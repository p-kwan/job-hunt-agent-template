#!/usr/bin/env python3
"""Query SerpApi's Google Jobs engine and print structured results.

Reads SERPAPI_KEY from the environment (source .env before running).
Stdlib-only — no dependencies to install.

Usage:
    python3 scripts/search_jobs.py "entry level mechanical engineer" --location "San Francisco Bay Area" --num 20
    python3 scripts/search_jobs.py "..." --sources all       # no filtering, every aggregator Google Jobs indexes
    python3 scripts/search_jobs.py "..." --sources quality   # default: company career pages + LinkedIn only
"""
import argparse
import json
import os
import sys
import urllib.parse
import urllib.request

API_URL = "https://serpapi.com/search.json"

# "quality" mode excludes postings whose `via` field matches a known
# generic aggregator/reposting site, keeping LinkedIn and (usually)
# direct company-career-page / ATS-hosted postings. Edit this list to
# retune which boards count as noise vs signal.
BLOCKED_AGGREGATORS = [
    "indeed", "ziprecruiter", "glassdoor", "built in", "builtin",
    "jobleads", "learn4good", "wayup", "simplyhired", "monster",
    "careerbuilder", "jobright", "talentify", "prosple", "adzuna",
    "recruit.net", "jobg8", "jora", "neuvoo", "getwork", "trabajo.org",
]


def search_jobs(query: str, location: str | None, api_key: str) -> dict:
    params = {"engine": "google_jobs", "q": query, "api_key": api_key}
    if location:
        params["location"] = location
    url = f"{API_URL}?{urllib.parse.urlencode(params)}"
    with urllib.request.urlopen(url, timeout=30) as resp:
        return json.load(resp)


def passes_source_filter(via: str, sources: str) -> bool:
    if sources == "all":
        return True
    via_lower = via.lower()
    return not any(blocked in via_lower for blocked in BLOCKED_AGGREGATORS)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="Search query, e.g. 'entry level mechanical engineer'")
    parser.add_argument("--location", default=None, help="Location filter, e.g. 'San Francisco Bay Area'")
    parser.add_argument("--num", type=int, default=10, help="Max results to print (default 10)")
    parser.add_argument(
        "--sources",
        choices=["quality", "all"],
        default="quality",
        help="'quality' (default) = company career pages + LinkedIn only, filters out generic aggregators. 'all' = no filtering.",
    )
    args = parser.parse_args()

    api_key = os.environ.get("SERPAPI_KEY")
    if not api_key:
        print("ERROR: SERPAPI_KEY not set. Run: set -a && source .env && set +a", file=sys.stderr)
        return 1

    try:
        data = search_jobs(args.query, args.location, api_key)
    except Exception as e:
        print(f"ERROR: request failed: {e}", file=sys.stderr)
        return 1

    if "error" in data:
        print(f"ERROR: {data['error']}", file=sys.stderr)
        return 1

    all_jobs = data.get("jobs_results", [])
    filtered_out = 0
    jobs = []
    for job in all_jobs:
        via = job.get("via", "")
        if passes_source_filter(via, args.sources):
            jobs.append(job)
        else:
            filtered_out += 1
    jobs = jobs[: args.num]

    if not jobs:
        print("No results after filtering." if filtered_out else "No results.")
        if filtered_out:
            print(f"({filtered_out} result(s) filtered out by --sources quality; use --sources all to see them)")
        return 0

    for i, job in enumerate(jobs, 1):
        title = job.get("title", "?")
        company = job.get("company_name", "?")
        location = job.get("location", "?")
        via = job.get("via", "?")
        posted = job.get("detected_extensions", {}).get("posted_at", "?")
        schedule = job.get("detected_extensions", {}).get("schedule_type", "?")
        apply_links = job.get("apply_options", [])
        link = apply_links[0]["link"] if apply_links else job.get("share_link", "?")
        description = (job.get("description") or "").strip().replace("\n", " ")[:300]

        print(f"[{i}] {title}")
        print(f"    Company:  {company}")
        print(f"    Location: {location}")
        print(f"    Via:      {via}  |  Posted: {posted}  |  Type: {schedule}")
        print(f"    Link:     {link}")
        print(f"    Desc:     {description}...")
        print()

    if filtered_out:
        print(f"({filtered_out} additional result(s) filtered out by --sources quality; use --sources all to see them)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
