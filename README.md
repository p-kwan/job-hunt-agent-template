# Job Hunt Agent (Template)

A personal job-hunt agent template, built to run inside Claude Code. The agent itself is a small set of markdown files that Claude reads and updates — there's no separate app to run for the core workflow.

## Getting started

1. Open this folder in Claude Code.
2. Open [`job_search_profile.md`](job_search_profile.md) and ask Claude to interview you and fill it in — see [`CLAUDE.md`](CLAUDE.md) for the exact prompt pattern, or just say: "Open job_search_profile.md and ask me the questions needed to fill it in, then draft it based on my answers."
3. (Optional) Give Claude a SearchAPI.io or SerpApi.com API key for real structured job search results — paste it directly in chat (e.g. "Here's my SerpAPI key: ...") and Claude will store it in `.env`, never in a tracked file.
4. Paste the contents of [`weekly_run_prompt.md`](weekly_run_prompt.md) any time you want to run a search cycle.

## Files

- [`job_search_profile.md`](job_search_profile.md) — target roles, locations, industries, and constraints. The source of truth for what counts as a good lead. Starts blank — fill it in first.
- [`weekly_job_hunt_workflow.md`](weekly_job_hunt_workflow.md) — the numbered procedure Claude follows each run: search for postings, screen them against the profile, update the leads log, flag anything needing attention, and summarize. Never applies or messages anyone without explicit confirmation.
- [`job_leads.md`](job_leads.md) — running log of saved leads (company, role, link, status, notes). Starts empty.
- [`weekly_run_prompt.md`](weekly_run_prompt.md) — the prompt to paste into Claude Code to kick off a run.
- [`scheduled_run_prompt.md`](scheduled_run_prompt.md) — a variant of the run prompt written for unattended/scheduled execution (e.g. a cloud cron routine), if you want this to run automatically on a schedule.
- [`CLAUDE.md`](CLAUDE.md) — guidance for Claude Code on how these files fit together.
- [`scripts/search_jobs.py`](scripts/search_jobs.py) — a small CLI that queries SerpApi's Google Jobs engine for structured, dated job listings. Optional — Claude falls back to general web search if no API key is set.

## Secrets

Any API key goes in `.env` (gitignored, created automatically the first time you give Claude one) — never in a tracked file. `.env.example` documents the expected variable names.

## Python scaffold (unused)

`src/job_search_agent/` and `tests/` are a minimal, currently-unused Python skeleton kept in case a coded tool (e.g. a scraper) is needed later.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```
