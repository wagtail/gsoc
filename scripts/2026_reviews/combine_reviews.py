# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Combine GSoC proposal review CSVs into a single output.

Joins three CSV sources on proposal_id:
- GSoC_proposals_2026_wagtail_all_20260401-040447.csv (base export)
- gsoc_proposals_review.csv (GitHub contribution data)
- proposals_llm_review.csv (LLM-based content review)

Shared columns are kept once (from the first source that has them).

Usage:
    uv run combine_reviews.py
    uv run combine_reviews.py --output combined.csv
"""

import argparse
import csv
from pathlib import Path

BASE_DIR = Path(__file__).parent

SOURCES = [
    # (path, label) - ordered by priority for shared column names
    (BASE_DIR / "gsoc_proposals_review.csv", "review"),
    (BASE_DIR / "proposals_llm_review.csv", "llm"),
]

# The base GSoC export is already included in gsoc_proposals_review.csv
# (which adds review_* columns to it). We use that as the primary source
# and only pull *new* columns from the LLM review.

DEFAULT_OUTPUT = BASE_DIR / "proposals_combined.csv"

# Columns to rename in the combined output (old_name -> new_name)
COLUMN_RENAMES = {
    "target_project": "llm_target_project",
    "target_size": "llm_target_size",
    "ai_writing_assessment": "llm_writing_assessment",
}

# Value mappings for specific columns (applied after rename, keyed by new name)
VALUE_TRANSFORMS = {
    "llm_target_project": {
        "demo-redesign": "Demo website redesign",
        "starter-kit": "Starter kit upgrade",
        "multilingual": "Multilingual support improvements",
        "bespoke-idea": "Bespoke idea",
        "wrong-org": "Wrong organisation",
        "nonsense": "Nonsense",
    },
    "llm_writing_assessment": {
        "likely-heavy-ai": "Likely heavy AI",
        "mixed": "Mixed",
        "likely-human": "Likely human",
    },
    "has_ai_disclosure": {
        "yes": "Yes",
        "no": "No",
    },
}


def load_csv(path: Path) -> tuple[list[str], dict[str, dict]]:
    """Load a CSV into (fieldnames, {proposal_id: row})."""
    rows_by_id = {}
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames or [])
        for row in reader:
            pid = row.get("proposal_id", "").strip()
            if pid:
                rows_by_id[pid] = row
    return fieldnames, rows_by_id


def main():
    parser = argparse.ArgumentParser(description="Combine GSoC review CSVs")
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Output CSV path (default: {DEFAULT_OUTPUT})",
    )
    args = parser.parse_args()

    # Load all sources
    loaded = []
    for path, label in SOURCES:
        if not path.exists():
            print(f"WARNING: {path.name} not found, skipping")
            continue
        fieldnames, rows = load_csv(path)
        print(f"Loaded {path.name}: {len(rows)} rows, {len(fieldnames)} columns")
        loaded.append((label, fieldnames, rows))

    if not loaded:
        print("ERROR: No source files found")
        return

    # Use the first source (gsoc_proposals_review.csv) as the base
    base_label, base_fields, base_rows = loaded[0]

    # Collect new columns from additional sources (preserving order, no dupes)
    seen_fields = set(base_fields)
    combined_fields = list(base_fields)

    # Track which columns come from which source for the summary
    source_columns = {base_label: list(base_fields)}

    for label, fieldnames, rows in loaded[1:]:
        new_cols = []
        for f in fieldnames:
            if f not in seen_fields and f != "proposal_id":
                seen_fields.add(f)
                combined_fields.append(f)
                new_cols.append(f)
        source_columns[label] = new_cols

    # Merge: start from base rows, enrich with additional sources
    all_ids = list(base_rows.keys())

    # Also pick up any IDs only present in other sources
    for label, fieldnames, rows in loaded[1:]:
        for pid in rows:
            if pid not in base_rows:
                all_ids.append(pid)

    combined_rows = []
    match_counts = {label: 0 for label, _, _ in loaded[1:]}

    for pid in all_ids:
        row = {}
        # Start with base data
        if pid in base_rows:
            row.update(base_rows[pid])

        # Layer on additional sources
        for label, fieldnames, rows in loaded[1:]:
            if pid in rows:
                match_counts[label] += 1
                for f in fieldnames:
                    if f in seen_fields and f not in row:
                        row[f] = rows[pid].get(f, "")
                    elif f in source_columns.get(label, []):
                        row[f] = rows[pid].get(f, "")

        combined_rows.append(row)

    # Apply column renames
    combined_fields = [COLUMN_RENAMES.get(f, f) for f in combined_fields]
    for row in combined_rows:
        for old_name, new_name in COLUMN_RENAMES.items():
            if old_name in row:
                row[new_name] = row.pop(old_name)
        # Apply value transforms
        for col, mapping in VALUE_TRANSFORMS.items():
            if col in row:
                row[col] = mapping.get(row[col], row[col])

    # Write output
    with open(args.output, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=combined_fields)
        writer.writeheader()
        writer.writerows(combined_rows)

    print(f"\nOutput: {args.output}")
    print(f"Combined rows: {len(combined_rows)}")
    print(f"Combined columns: {len(combined_fields)}")

    print("\nColumn sources:")
    for label, cols in source_columns.items():
        print(f"  {label}: {len(cols)} columns")

    print("\nJoin matches:")
    for label, count in match_counts.items():
        total = len(loaded[0][2])
        print(f"  {label}: {count}/{total} base rows matched")

    unmatched_base = set(base_rows.keys())
    for label, fieldnames, rows in loaded[1:]:
        unmatched = unmatched_base - set(rows.keys())
        if unmatched:
            print(f"\n  {len(unmatched)} base rows had no match in {label}:")
            for pid in sorted(unmatched)[:10]:
                print(f"    - {pid}")
            if len(unmatched) > 10:
                print(f"    ... and {len(unmatched) - 10} more")


if __name__ == "__main__":
    main()
