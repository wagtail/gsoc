#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "anthropic>=0.42.0",
# ]
# ///
"""
Review GSoC proposals using Claude API.

Reads all .md proposals from the proposals/ directory, sends each to Claude
for structured assessment, and outputs a CSV summary.

Usage:
    uv run review_proposals_llm.py
    uv run review_proposals_llm.py --model claude-haiku-4-5-20251001
    uv run review_proposals_llm.py --max 10  # process only first 10 for testing
"""

import argparse
import csv
import json
import sys
import time
from pathlib import Path

import anthropic

PROPOSALS_DIR = Path(__file__).parent / "proposals"
OUTPUT_CSV = Path(__file__).parent / "proposals_llm_review.csv"

PROJECT_IDEAS = """\
1. **Demo website redesign** (350h) – Redesign of the Wagtail bakery demo site \
(bakerydemo), implementing new visual design, new site sections, refactorings. \
Skills: front-end (Django, HTML, CSS), backend (Django, Python). \
Mentors: Thibaud Colas. Discussion: #133.

2. **Starter kit upgrade** (350h) – Iterate on the Wagtail news-template starter \
kit so it better serves as the best starting point for Wagtail. Automation to \
keep it up-to-date, possibly different variations. \
Skills: backend (Django, Python), DevOps. Mentors: Meagen Voss. Discussion: #134.

3. **Multilingual support improvements** (350h) – Improvements to Wagtail's i18n \
capabilities in core and packages like wagtail-localize. Based on community \
feedback in discussion #13693. Bug fixes, translation workflow automation, \
documentation. Skills: i18n, backend (Django, Python). \
Mentors: Thibaud Colas, Coen van der Kamp, Sævar Öfjörð Magnússon. Discussion: #135.

4. **Your own idea** – Contributors can propose their own project idea, provided \
it's useful for the Wagtail project, well-scoped, and achievable. Discussion: #136.
"""

REVIEW_PROMPT = """\
You are reviewing a Google Summer of Code (GSoC) 2026 proposal for the Wagtail \
open-source CMS project (built on Django/Python).

Here are the official project ideas for this year:

{project_ideas}

Analyze the following proposal and return a JSON object (no markdown fencing) with these fields:

1. "target_project": one of "demo-redesign", "starter-kit", "multilingual", "bespoke-idea", "wrong-org", "nonsense"
   - "wrong-org" = proposal is clearly for a different organisation/project (e.g. Webpack, LibreOffice)
   - "nonsense" = incoherent, extremely low effort, or spam
   - "bespoke-idea" = proposes something for Wagtail but not one of the three listed projects
2. "target_project_confidence": 1-5 (how clearly it maps)
3. "ai_writing_assessment": one of "likely-heavy-ai", "mixed", "likely-human"
4. "ai_writing_signals": brief explanation (max 2 sentences) of why you gave that rating
5. "quality_score": 1-10 overall quality score where:
   - 1-2: spam, nonsense, or wrong organisation
   - 3-4: very low effort, no real substance, generic filler
   - 5-6: adequate structure but lacking depth, specificity, or Wagtail knowledge
   - 7-8: solid proposal with good technical understanding and planning
   - 9-10: exceptional - deep Wagtail knowledge, real contributions, specific and feasible plan
6. "quality_summary": 2-3 sentence qualitative assessment
7. "has_schedule": boolean
8. "has_prior_contributions": boolean - do they reference actual Wagtail PRs/issues/contributions?
9. "has_implementation_detail": boolean - do they describe specific technical approach?
10. "references_wagtail_internals": boolean - do they reference actual Wagtail code, issues, or PRs by number?
11. "target_size": the project size stated in the proposal. Use one of: "350h", "175h", "90h", or "unclear" if not stated
12. "has_ai_disclosure": boolean - does the proposal include a section or statement about AI tool usage?
13. "red_flags": list of strings, any concerns (empty list if none). Examples: "no Wagtail experience mentioned", "proposal appears to be for wrong org", "schedule is unrealistic"

Proposal:

{proposal}
"""


def parse_args():
    parser = argparse.ArgumentParser(description="Review GSoC proposals with Claude")
    parser.add_argument(
        "--model",
        default="claude-haiku-4-5-20251001",
        help="Anthropic model to use (default: claude-haiku-4-5-20251001)",
    )
    parser.add_argument(
        "--max",
        type=int,
        default=0,
        help="Max proposals to process (0 = all)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=OUTPUT_CSV,
        help=f"Output CSV path (default: {OUTPUT_CSV})",
    )
    return parser.parse_args()


def load_proposals(max_count: int = 0) -> list[tuple[str, str]]:
    """Load all .md proposals. Returns list of (filename, content)."""
    files = sorted(PROPOSALS_DIR.glob("*.md"))
    if max_count > 0:
        files = files[:max_count]
    proposals = []
    for f in files:
        content = f.read_text(encoding="utf-8", errors="replace")
        proposals.append((f.name, content))
    return proposals


def parse_filename(filename: str) -> tuple[str, str]:
    """Split filename into (proposal_id, github_username) on first underscore."""
    stem = Path(filename).stem
    if "_" in stem:
        proposal_id, username = stem.split("_", 1)
        return proposal_id, username
    return stem, ""


def review_proposal(
    client: anthropic.Anthropic, model: str, filename: str, content: str
) -> dict:
    """Send a single proposal to Claude for review. Returns parsed JSON."""
    prompt = REVIEW_PROMPT.format(project_ideas=PROJECT_IDEAS, proposal=content)

    for attempt in range(3):
        try:
            response = client.messages.create(
                model=model,
                max_tokens=1024,
                messages=[{"role": "user", "content": prompt}],
            )
            text = response.content[0].text.strip()
            # Strip markdown fencing if present despite instructions
            if text.startswith("```"):
                text = text.split("\n", 1)[1]
                if text.endswith("```"):
                    text = text[: text.rfind("```")]
            return json.loads(text)
        except json.JSONDecodeError:
            print(
                f"  WARNING: JSON parse error for {filename} (attempt {attempt + 1})",
                file=sys.stderr,
            )
            if attempt == 2:
                return {"error": "JSON parse failure", "raw": text[:200]}
        except anthropic.RateLimitError:
            wait = 2 ** (attempt + 1)
            print(f"  Rate limited, waiting {wait}s...", file=sys.stderr)
            time.sleep(wait)
        except anthropic.APIError as e:
            print(f"  API error for {filename}: {e}", file=sys.stderr)
            if attempt == 2:
                return {"error": str(e)}

    return {"error": "max retries exceeded"}


CSV_FIELDS = [
    "filename",
    "proposal_id",
    "github_username",
    "target_project",
    "target_project_confidence",
    "target_size",
    "ai_writing_assessment",
    "ai_writing_signals",
    "has_ai_disclosure",
    "quality_score",
    "quality_summary",
    "has_schedule",
    "has_prior_contributions",
    "has_implementation_detail",
    "references_wagtail_internals",
    "red_flags",
    "error",
]


def main():
    args = parse_args()
    proposals = load_proposals(args.max)
    print(f"Loaded {len(proposals)} proposals from {PROPOSALS_DIR}")
    print(f"Using model: {args.model}")
    print(f"Output: {args.output}")
    print()

    client = anthropic.Anthropic()

    results = []
    for i, (filename, content) in enumerate(proposals, 1):
        proposal_id, username = parse_filename(filename)
        label = username or filename
        print(f"[{i}/{len(proposals)}] Reviewing {label}...", end=" ", flush=True)

        review = review_proposal(client, args.model, filename, content)

        row = {"filename": filename, "proposal_id": proposal_id, "github_username": username}
        if "error" in review:
            row["error"] = review["error"]
            print(f"ERROR: {review['error']}")
        else:
            for field in CSV_FIELDS:
                if field in review:
                    val = review[field]
                    if isinstance(val, list):
                        val = "; ".join(val)
                    elif isinstance(val, bool):
                        val = "yes" if val else "no"
                    row[field] = val
            print(
                f"score={review.get('quality_score', '?')} "
                f"target={review.get('target_project', '?')}"
            )

        results.append(row)

    # Write CSV
    with open(args.output, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        writer.writeheader()
        writer.writerows(results)

    print(f"\nDone! Results written to {args.output}")

    # Print summary
    targets = {}
    ai_counts = {}
    scores = []
    for r in results:
        t = r.get("target_project", "error")
        targets[t] = targets.get(t, 0) + 1
        a = r.get("ai_writing_assessment", "unknown")
        ai_counts[a] = ai_counts.get(a, 0) + 1
        try:
            scores.append(int(r.get("quality_score", 0)))
        except (ValueError, TypeError):
            pass

    print("\n--- Summary ---")
    print("\nBy target project:")
    for k, v in sorted(targets.items(), key=lambda x: -x[1]):
        print(f"  {k}: {v}")
    print("\nBy AI writing assessment:")
    for k, v in sorted(ai_counts.items(), key=lambda x: -x[1]):
        print(f"  {k}: {v}")
    if scores:
        print(
            f"\nQuality scores: min={min(scores)} max={max(scores)} "
            f"avg={sum(scores) / len(scores):.1f}"
        )


if __name__ == "__main__":
    main()
