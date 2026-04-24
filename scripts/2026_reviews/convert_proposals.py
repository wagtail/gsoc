#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "docling",
# ]
# ///
"""Convert proposal PDFs to Markdown with YAML frontmatter."""

import csv
import os
import glob

from docling.document_converter import DocumentConverter

CSV_FILE = "GSoC_proposals_2026_wagtail_all_20260401-040447.csv"
PROPOSALS_DIR = "proposals"
PARTICIPANTS_DIR = "2026/participants"

# Build lookup from proposal_id to CSV row
with open(CSV_FILE) as f:
    reader = csv.DictReader(f)
    rows_by_id = {row["proposal_id"]: row for row in reader}

# Build set of participant files (lowercase for case-insensitive matching)
participant_files = {}
for name in os.listdir(PARTICIPANTS_DIR):
    if name.endswith(".md") and name != "template.md":
        participant_files[name.removesuffix(".md").lower()] = name.removesuffix(".md")

# Get all PDFs
pdfs = sorted(glob.glob(os.path.join(PROPOSALS_DIR, "*.pdf")))
print(f"Found {len(pdfs)} PDFs to convert")

converter = DocumentConverter()

for i, pdf_path in enumerate(pdfs, 1):
    basename = os.path.basename(pdf_path)
    md_path = pdf_path.removesuffix(".pdf") + ".md"

    if os.path.exists(md_path):
        print(f"  [{i}/{len(pdfs)}] {basename} — already converted, skipping")
        continue

    # Extract proposal_id and github_username from filename
    name = basename.removesuffix(".pdf")
    if "_" in name:
        proposal_id, github_username = name.split("_", 1)
    else:
        proposal_id = name
        github_username = ""

    # Look up CSV data
    row = rows_by_id.get(proposal_id, {})
    csv_username = github_username or row.get("github_username", "").strip()
    # Clean up CSV username the same way as download script
    if csv_username:
        csv_username = csv_username.rstrip("/").split("/")[-1].lstrip("@").replace(" ", "-")

    # Build frontmatter
    frontmatter_lines = ["---"]
    if csv_username:
        frontmatter_lines.append(f"github_username: {csv_username}")
        # Check for participant file (case-insensitive)
        participant_name = participant_files.get(csv_username.lower())
        if participant_name:
            frontmatter_lines.append(
                f"participant: 2026/participants/{participant_name}.md"
            )
        frontmatter_lines.append(
            f"gh_search: https://github.com/search?q=org%3Awagtail+involves%3A{csv_username}&type=issues"
        )
    frontmatter_lines.append("---")
    frontmatter = "\n".join(frontmatter_lines) + "\n\n"

    print(f"  [{i}/{len(pdfs)}] Converting {basename}...", end=" ", flush=True)

    try:
        doc = converter.convert(pdf_path).document
        markdown = doc.export_to_markdown()

        with open(md_path, "w") as f:
            f.write(frontmatter)
            f.write(markdown)
            f.write("\n")

        print("OK")
    except Exception as e:
        print(f"ERROR: {e}")

print("Done!")
