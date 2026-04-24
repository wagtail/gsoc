#!/usr/bin/env python3
"""Download GSoC 2026 proposal PDFs from the CSV export."""

import csv
import os
import subprocess
import time

CSV_FILE = "GSoC_proposals_2026_wagtail_all_20260401-040447.csv"
OUTPUT_DIR = "proposals"

COOKIE = os.getenv("GSOC_COOKIE")
USER_AGENT = os.getenv("USER_AGENT")

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(CSV_FILE) as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print(f"Found {len(rows)} proposals")

success = 0
failed = 0

for i, row in enumerate(rows, 1):
    proposal_id = row["proposal_id"]
    github_username = row["github_username"].strip()
    pdf_url = row["project_pdf"].strip()

    if not pdf_url:
        print(f"  [{i}/{len(rows)}] {proposal_id} — no PDF URL, skipping")
        failed += 1
        continue

    # Clean up github_username: strip URLs, @, and replace spaces
    if github_username:
        github_username = github_username.rstrip("/").split("/")[-1]
        github_username = github_username.lstrip("@").replace(" ", "-")

    if github_username:
        filename = f"{proposal_id}_{github_username}.pdf"
    else:
        filename = f"{proposal_id}.pdf"

    filepath = os.path.join(OUTPUT_DIR, filename)

    if os.path.exists(filepath):
        print(f"  [{i}/{len(rows)}] {filename} — already exists, skipping")
        success += 1
        continue

    print(f"  [{i}/{len(rows)}] Downloading {filename}...", end=" ", flush=True)

    result = subprocess.run(
        [
            "curl",
            "-s",
            "-o",
            filepath,
            "-w",
            "%{http_code}",
            "-b",
            COOKIE,
            "-H",
            f"user-agent: {USER_AGENT}",
            pdf_url,
        ],
        capture_output=True,
        text=True,
    )

    status = result.stdout.strip()
    if status == "200":
        print("OK")
        success += 1
    else:
        print(f"HTTP {status}")
        # Remove empty/error files
        if os.path.exists(filepath):
            os.remove(filepath)
        failed += 1

    time.sleep(0.3)

print(f"\nDone! {success} downloaded, {failed} failed.")
