# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project status

This is a personal job-hunt agent. The actual "agent" is Claude Code operating over a small set of markdown files, not the Python package below — treat the markdown workflow as primary.

## Job hunt files

- [job_search_profile.md](job_search_profile.md) — target roles, locations, industries, and hard constraints (comp floor, visa, remote preference). Read this before searching for or judging any lead.
- [weekly_job_hunt_workflow.md](weekly_job_hunt_workflow.md) — the repeatable procedure to follow on each run: load context, find new leads, screen against constraints, update the leads file, summarize, and never apply/send anything without explicit confirmation.
- [job_leads.md](job_leads.md) — the running log of leads (table: date, company, role, link, status, notes). This is the source of truth for what's already been found and its status — check it before adding a "new" lead to avoid duplicates.
- [weekly_run_prompt.md](weekly_run_prompt.md) — the exact prompt the user pastes to kick off a run. When invoked, execute `weekly_job_hunt_workflow.md` using the other two files as described above.

When the user asks to "run the weekly job hunt" (or pastes the contents of `weekly_run_prompt.md`), follow `weekly_job_hunt_workflow.md` step by step rather than improvising a different process.

## Search tooling

[scripts/search_jobs.py](scripts/search_jobs.py) is the primary job search tool (step 4 of the workflow) — a stdlib-only CLI that queries SerpApi's Google Jobs engine and prints structured results (title, company, location, posting age, apply link). Requires `SERPAPI_KEY` in `.env`:

```bash
set -a && source .env && set +a && python3 scripts/search_jobs.py "<query>" --location "San Francisco Bay Area" --num 20
```

`WebSearch`/`WebFetch` remain in use for: (a) fallback if the script errors, and (b) verifying that a specific posting found via the script is still live before logging it — the script surfaces aggregator results, which still need confirming against the real posting. There's also a working `SEARCHAPI_KEY` in `.env` (SearchAPI.io, same Google Jobs engine) not currently wired into the workflow — a reasonable second option if SerpApi's key stops working or rate-limits.

## Secrets management

Any API key or credential this project ever needs goes in `.env` (gitignored) — never hardcoded in a committed file, never pasted into `job_leads.md` or any other tracked markdown. `.env.example` documents the expected variable names with empty values. Before adding a new key: add its name (no value) to `.env.example`, and confirm with the user before writing the real value anywhere.

## Python skeleton (unused)

`src/job_search_agent/` and `tests/` are a minimal Python scaffold created early on — unrelated to `scripts/search_jobs.py` and still unused. Don't build it out unless the user explicitly asks for a coded tool beyond job search (e.g. an app or CLI wrapper) — the markdown-driven workflow plus the search script is the current direction.

## Commands

```bash
# One-time setup
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"

# Run
python -m job_search_agent.main

# Test (all)
pytest

# Test (single file / single test)
pytest tests/test_main.py
pytest tests/test_main.py::test_main_runs
```

There is no linter or type checker configured yet — add one (e.g. ruff, mypy) when the project's needs become clearer, rather than assuming a specific tool.

## Architecture

- `src/` layout: importable code lives under `src/job_search_agent/`, installed in editable mode via `pyproject.toml` (setuptools backend). Tests import it as the `job_search_agent` package, not by relative path.
- `tests/` mirrors the package for pytest discovery.
- No external dependencies are declared yet (`dependencies = []` in `pyproject.toml`); `pytest` is a dev-only extra.
