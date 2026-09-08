# Scheduled Run Prompt (Automated)

This is the prompt the weekly cron job runs. Unlike [weekly_run_prompt.md](weekly_run_prompt.md) (which you paste yourself and which pauses to ask you to confirm/update your profile), this version runs unattended — it never waits for an answer — and ends by messaging you a summary instead of just replying in a chat you're watching.

---

Run the weekly job hunt for the Job Hunt project autonomously:

1. Run the weekly job hunt per `weekly_job_hunt_workflow.md`, using `job_search_profile.md` for targeting (including its "Search sources" mode) and `scripts/search_jobs.py` for search. This includes re-verifying existing leads' links before adding anything new.
2. Update `job_leads.md` with anything new.
3. Pick the single best-fit new lead from this run and draft one outreach email for it — draft only, never send it.
4. Commit and push all changes to git with a clear commit message.
5. Send a message summarizing: new leads found, leads marked `passed` (dead links or no longer fitting criteria), anything needing attention, and the full text of the drafted outreach email, ready to review and send.

Do not ask clarifying questions during this run — if something is ambiguous, make the most reasonable call consistent with `job_search_profile.md`, note it in the summary, and continue. Never send any email or message on the user's behalf other than the summary in step 5 — drafting is automatic, sending never is.

---
