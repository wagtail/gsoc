# GSoC scripts

## 2026 Proposal review pipeline

One-off scripts to process and review GSoC proposals. Run them in sequence from the repo root (not from `scripts/2026_reviews/`).

### Prerequisites

- [uv](https://docs.astral.sh/uv/)
- [GitHub CLI](https://cli.github.com/)
- `ANTHROPIC_API_KEY` environment variable
- The GSoC proposals CSV export: `GSoC_proposals_2026_wagtail_all_20260401-040447.csv`
- A `blocked.txt` file listing blocked GitHub usernames, one per line

### 1. Download proposal PDFs — `download_proposals.py`

Downloads proposal PDFs from the GSoC site using the CSV export's `project_pdf` URLs. Requires authenticated session cookies because the GSoC site has no public API.

```sh
GSOC_COOKIE="<your-cookie-string>" USER_AGENT="<your-browser-ua>" python scripts/2026_reviews/download_proposals.py
```

Output: `proposals/<proposal_id>_<github_username>.pdf` files.

### 2. Convert PDFs to Markdown — `convert_proposals.py`

Converts each PDF to Markdown using [docling](https://github.com/docling-project/docling), and prepends YAML frontmatter with GitHub username, participant file link, and a Wagtail org search URL.

```sh
uv run scripts/2026_reviews/convert_proposals.py
```

Output: `proposals/<proposal_id>_<github_username>.md` files alongside the PDFs.

**Limitations:** PDF-to-Markdown conversion is lossy — tables, images, and complex layouts may not convert cleanly. The first run is slow as docling downloads its models. Skips already-converted files.

### 3. Enrich with GitHub data — `review_proposals.py`

Reads the CSV export and, for each proposal, checks whether the applicant is blocked and fetches their contribution stats (issues opened/resolved, involvement) across `wagtail/wagtail`, `wagtail/bakerydemo`, and `wagtail/news-template` via `gh search issues`.

⚠️ those metrics reflect a very narrow understanding of contributors’ online involvement, so should only be used for a baseline check, not decisions.

```sh
uv run scripts/2026_reviews/review_proposals.py
```

Output: `gsoc_proposals_review.csv` — the original CSV columns plus `review_blocked`, `review_ratio_*`, `review_github_search_url`, and `review_participant_file`.

### 4. LLM-based proposal review — `review_proposals_llm.py`

Sends each Markdown proposal to the Anthropic API for structured assessment: target project classification, quality score (1–10), AI-writing detection, schedule/contribution checks, and red flags.

⚠️ LLM assessments are prone to a lot of issues. This is only for a baseline check "looks AI-generated yes/no"; "low-quality yes/no". Shouldn’t be used to decide on shortlisted proposals.

```sh
uv run scripts/2026_reviews/review_proposals_llm.py
# Use a different model:
uv run scripts/2026_reviews/review_proposals_llm.py --model claude-sonnet-4-20250514
# Test with a subset:
uv run scripts/2026_reviews/review_proposals_llm.py --max 5
```

Output: `scripts/2026_reviews/proposals_llm_review.csv`.

### 5. Combine all reviews — `combine_reviews.py`

Joins `gsoc_proposals_review.csv` (step 3) and `proposals_llm_review.csv` (step 4) on `proposal_id` into a single CSV for spreadsheet review.

```sh
uv run scripts/2026_reviews/combine_reviews.py
```

Output: `scripts/2026_reviews/proposals_combined.csv`.

