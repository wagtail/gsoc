#!/usr/bin/env -S uv run
"""
GSoC Proposal Review Script

Processes GSoC proposals CSV and generates enhanced CSV with:
- Blocked user status
- GitHub contribution ratios for 3 repos (using cached data)
- Participant file links
- All original CSV fields retained
"""

import csv
import json
import os
import re
import subprocess
from pathlib import Path
from typing import Dict, List, Optional
import time


def load_csv_with_multiline(filepath: str) -> List[Dict]:
    """Load CSV file handling multiline strings properly."""
    rows = []
    with open(filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


def load_blocked_users(filepath: str) -> set:
    """Load blocked users from text file."""
    blocked = set()
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            username = line.strip()
            if username and not username.startswith("#"):
                blocked.add(username.lower())
    return blocked


def is_blocked(username: str, blocked_set: set) -> bool:
    """Check if username is in blocked set (case-insensitive)."""
    if not username:
        return False
    return username.lower() in blocked_set


def extract_github_username(github_url: str) -> Optional[str]:
    """Extract username from GitHub URL."""
    if not github_url:
        return None
    patterns = [
        r"github\.com/([^/]+)/?$",
        r"github\.com/([^/]+)/[^/]+/?$",
    ]
    for pattern in patterns:
        match = re.search(pattern, github_url)
        if match:
            return match.group(1)
    return None


def gh_get_user_issues(repo: str, username: str) -> str:
    """
    Use GitHub CLI to get issues/PRs for a specific user.
    Returns ratio string like "2/6:0".
    """
    if not username:
        return "0/0:0"

    try:
        # Get issues/PRs created by user using --repo and --author flags
        result_created = subprocess.run(
            [
                "gh",
                "search",
                "issues",
                "--repo",
                repo,
                "--author",
                username,
                "--json",
                "state",
            ],
            capture_output=True,
            text=True,
            timeout=15,
        )

        # Get issues where user is involved
        result_involved = subprocess.run(
            [
                "gh",
                "search",
                "issues",
                "--repo",
                repo,
                "--involves",
                username,
                "--json",
                "state",
            ],
            capture_output=True,
            text=True,
            timeout=15,
        )

        opened = 0
        resolved = 0

        if result_created.returncode == 0:
            items = json.loads(result_created.stdout) if result_created.stdout else []
            for item in items:
                state = item.get("state", "").lower()
                opened += 1
                if state == "closed":
                    resolved += 1

        assists = 0
        if result_involved.returncode == 0:
            items = json.loads(result_involved.stdout) if result_involved.stdout else []
            assists = len(items)

        return f"{resolved}/{opened}:{assists}"

    except Exception as e:
        print(f"    Error: {e}")
        return "0/0:0"


def get_cache_path(username: str, repo: str) -> Path:
    """Get cache file path for a user/repo combination."""
    cache_dir = Path(".gh_cache")
    cache_dir.mkdir(exist_ok=True)
    safe_name = re.sub(r"[^a-zA-Z0-9_-]", "_", f"{username}_{repo.replace('/', '_')}")
    return cache_dir / f"{safe_name}.json"


def load_cached_result(cache_path: Path) -> Optional[str]:
    """Load cached result if it exists and is fresh (24 hours)."""
    if cache_path.exists():
        try:
            with open(cache_path, "r") as f:
                data = json.load(f)
                if time.time() - data.get("timestamp", 0) < 86400:
                    return data.get("result")
        except:
            pass
    return None


def save_cached_result(cache_path: Path, result: str):
    """Save result to cache."""
    with open(cache_path, "w") as f:
        json.dump({"result": result, "timestamp": time.time()}, f)


def get_github_ratio(username: str, repo: str, use_cache: bool = True) -> str:
    """Get GitHub ratio with optional caching."""
    if not username:
        return "0/0:0"

    cache_path = get_cache_path(username, repo)

    # Check cache first if enabled
    if use_cache:
        cached = load_cached_result(cache_path)
        if cached:
            return cached

    # Fetch from API
    ratio = gh_get_user_issues(repo, username)

    # Save to cache
    save_cached_result(cache_path, ratio)

    # Rate limiting - be nice to the API
    time.sleep(0.5)

    return ratio


def find_participant_file(username: str, participants_dir: str) -> Optional[str]:
    """Find participant file for a username."""
    if not username:
        return None

    participants_path = Path(participants_dir)
    if not participants_path.exists():
        return None

    username_lower = username.lower()

    # Try exact match first
    for file in participants_path.glob("*.md"):
        if file.stem.lower() == username_lower:
            return str(file)

    # Try contains match
    for file in participants_path.glob("*.md"):
        file_base = file.stem.lower()
        if username_lower in file_base or file_base in username_lower:
            return str(file)

    return None


def generate_github_search_url(username: str) -> str:
    """Generate GitHub search URL for Wagtail org."""
    if not username:
        return ""
    return (
        f"https://github.com/search?q=org%3Awagtail+involves%3A{username}&type=issues"
    )


def process_proposals(
    csv_path: str,
    blocked_path: str,
    participants_dir: str,
    output_csv: str,
    refresh_github: bool = False,
):
    """Main processing function."""

    print("Loading data...")
    proposals = load_csv_with_multiline(csv_path)
    blocked_users = load_blocked_users(blocked_path)

    print(f"Loaded {len(proposals)} proposals")
    print(f"Loaded {len(blocked_users)} blocked users")

    # Check for existing cache
    cache_dir = Path(".gh_cache")
    cached_count = len(list(cache_dir.glob("*.json"))) if cache_dir.exists() else 0
    print(f"Found {cached_count} cached GitHub results")

    # Repositories to check
    repos = ["wagtail/wagtail", "wagtail/bakerydemo", "wagtail/news-template"]

    print("\nProcessing proposals...")
    print("Note: GitHub API calls are rate-limited (max 30 requests/minute)")
    print("Use --refresh to force refresh all GitHub data.\n")

    results = []

    for i, proposal in enumerate(proposals):
        contributor_name = proposal.get("contributor_display_name", "Unknown")
        print(f"[{i + 1}/{len(proposals)}] {contributor_name}", end="", flush=True)

        github_url = proposal.get("github_url", "")
        gh_username = extract_github_username(github_url)

        # Check if blocked
        blocked = is_blocked(gh_username, blocked_users) if gh_username else False
        if blocked:
            print(" [BLOCKED]", end="")

        # Get GitHub ratios
        ratios = {}
        if gh_username:
            print(" - fetching GitHub data...", end="", flush=True)
            for repo in repos:
                ratio = get_github_ratio(
                    gh_username, repo, use_cache=not refresh_github
                )
                ratios[repo] = ratio
            print(f" done (wagtail: {ratios['wagtail/wagtail']})")
        else:
            print(" - no GitHub")
            for repo in repos:
                ratios[repo] = "0/0:0"

        # Find participant file
        participant_file = find_participant_file(gh_username or "", participants_dir)

        # Generate GitHub search URL
        gh_search_url = generate_github_search_url(gh_username or "")

        # Build result row with ALL original fields plus new ones
        result = dict(proposal)  # Start with all original fields

        # Add new review fields
        result["review_blocked"] = "Yes" if blocked else "No"
        result["review_ratio_wagtail"] = ratios.get("wagtail/wagtail", "0/0:0")
        result["review_ratio_bakerydemo"] = ratios.get("wagtail/bakerydemo", "0/0:0")
        result["review_ratio_news_template"] = ratios.get(
            "wagtail/news-template", "0/0:0"
        )
        result["review_github_search_url"] = gh_search_url
        result["review_participant_file"] = participant_file or ""

        results.append(result)

    # Generate output CSV with all fields
    print(f"\nGenerating CSV: {output_csv}")
    with open(output_csv, "w", newline="", encoding="utf-8") as f:
        if results:
            writer = csv.DictWriter(f, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)

    print(f"\nDone! Processed {len(results)} proposals.")
    print(f"Output: {output_csv}")

    # Print summary
    blocked_count = sum(1 for r in results if r["review_blocked"] == "Yes")
    with_github = sum(
        1 for r in results if r.get("github_username") or r.get("github_url")
    )
    with_participant = sum(1 for r in results if r["review_participant_file"])

    print(f"\nSummary:")
    print(f"  Total proposals: {len(results)}")
    print(f"  Blocked users: {blocked_count}")
    print(f"  With GitHub profile: {with_github}")
    print(f"  With participant file: {with_participant}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Review GSoC proposals")
    parser.add_argument(
        "--csv", default="GSoC_proposals_2026_wagtail_all_20260401-040447.csv"
    )
    parser.add_argument("--blocked", default="blocked.txt")
    parser.add_argument("--participants", default="2026/participants")
    parser.add_argument("--output-csv", default="gsoc_proposals_review.csv")
    parser.add_argument(
        "--refresh", action="store_true", help="Force refresh all GitHub data"
    )

    args = parser.parse_args()

    process_proposals(
        csv_path=args.csv,
        blocked_path=args.blocked,
        participants_dir=args.participants,
        output_csv=args.output_csv,
        refresh_github=args.refresh,
    )
