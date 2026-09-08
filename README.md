# Job Hunt Agent (Template)

A personal job-hunt agent template, built to run inside Claude Code. The agent itself is a small set of markdown files that Claude reads and updates — there's no separate app to run for the core workflow.

## Getting started

1. **Get this folder onto your laptop — pick ONE of these, not both:**
   - **Download ZIP** (top of this repo page, under the green "Code" button) → unzip it. The unzipped folder is your project folder, done.
   - **Or clone it** in Terminal: `git clone <this-repo-url>` — this creates the same folder for you, just via git instead of a zip.
2. **Open that folder in Claude Code.** In Terminal: `cd` into the folder, then run `claude`.
   - The first time Claude Code runs in a folder it hasn't seen before, it asks whether you trust the files in this workspace — say yes. This is Claude Code's own one-time permission check before it will read or edit anything there.
   - If the folder lives inside Desktop, Documents, or Downloads, macOS may separately pop up its own "Terminal wants to access files in your ___ folder" dialog the first time — that's a normal macOS privacy prompt for Terminal itself, not something Claude is asking for. Click Allow/OK.
3. Open [`job_search_profile.md`](job_search_profile.md) and ask Claude to interview you and fill it in — see [`CLAUDE.md`](CLAUDE.md) for the exact prompt pattern, or just say: "Open job_search_profile.md and ask me the questions needed to fill it in, then draft it based on my answers."
4. (Optional) Give Claude a SearchAPI.io or SerpApi.com API key for real structured job search results — paste it directly in chat (e.g. "Here's my SerpAPI key: ...") and Claude will store it in `.env`, never in a tracked file.
5. Paste the contents of [`weekly_run_prompt.md`](weekly_run_prompt.md) any time you want to run a search cycle.

## Saving progress back to GitHub (optional)

Claude Code only edits the files on your laptop — it doesn't automatically sync anything to GitHub. If you cloned this from the template repo and want your changes (filled-in profile, saved leads, etc.) to actually show up on GitHub too, you need to **commit and push**, which requires the GitHub CLI installed and logged in on your machine:

1. Download and install it: go to [github.com/cli/cli/releases/latest](https://github.com/cli/cli/releases/latest) and get the `.pkg` installer for your Mac, then double-click to install.
2. In Terminal, run `gh auth login` and follow its prompts (GitHub.com → HTTPS → Yes → Login with a web browser).
3. Back in Claude Code, just ask: **"commit and push my changes"** — do this any time you want your latest edits to appear on your GitHub repo page.

This is a one-time setup per laptop. Until you do it, everything still works locally — you just won't see changes reflected on GitHub.

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
