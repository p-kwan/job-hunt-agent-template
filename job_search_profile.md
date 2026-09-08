# Job Search Profile

_Fill this in once; update as your search evolves. Claude reads this before searching for or evaluating leads._

## Target roles
- (e.g. Senior Product Manager, Staff Software Engineer, Entry-level Mechanical Engineer)
- Position types: full-time, internship/co-op, rotational program, or a mix — say which is the priority
- Note whether you want broad coverage (don't over-filter on exact title) or a narrow, specific match

## Target locations
- (e.g. Remote in US, San Francisco Bay Area, willing to relocate to ...)

## Target industries / companies
- Industries to prioritize:
- Companies of interest:
- Industries or companies to avoid:

## Search sources
- Mode: `quality` — company career pages + LinkedIn only. Generic aggregators/reposting sites (Indeed, ZipRecruiter, Glassdoor, Built In, JobLeads, Learn4Good, and similar — full list in `scripts/search_jobs.py`'s `BLOCKED_AGGREGATORS`) are filtered out.
- To change this: edit this line to `all` (no filtering — broadest coverage, more noise) or ask Claude to adjust the allow/block list in `scripts/search_jobs.py` for a custom source list.

## Constraints
- Compensation floor:
- Work authorization / visa status:
- Remote / hybrid / onsite preference:
- Company size preference (startup / mid-size / enterprise):
- Availability: when you can actually start (e.g. a graduation date, notice period, or "immediately"). Only postings matching this timing should be surfaced — say explicitly whether earlier/later postings should be dropped outright or just flagged.
- Anything else non-negotiable:

## Background summary
_A few sentences on experience level, key skills, and what makes a role a good fit — enough for Claude to judge a posting without re-reading a full resume each time. You can also just say "here's my resume" and share the file — Claude can read a PDF directly and draft this section for you._
