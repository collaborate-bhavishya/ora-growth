---
name: scout
description: Find this week's Founder Friday and Brand Teardown candidates from Indian D2C news, and pick the Tuesday AI topic. Use at the start of a weekly run or when asked to "scout", "find founders", or "find brands".
---

# Scout

Week folder: `pipeline/<YYYY>-W<ww>/` (ISO week of the posts' Monday). Create it if missing.

1. **AI topic:** `python3 scripts/tracker.py next-topic` → role | angle. If a major AI product launch relevant to D2C marketers happened in the last 7 days, propose it as an override (don't apply it without the user's OK).
2. **Brand category:** `python3 scripts/tracker.py next-category`.
3. **Founders:** WebSearch sources in `strategy/sources.md` for Indian D2C founders with a trigger in the last 30 days (funding, milestone, launch, expansion, Shark Tank India). Aim for 8–10. linkedin.com is blocked — don't try to fetch it.
4. **Brands:** 5 emerging Indian D2C brands (seed–Series C) in the category with a standout product.
5. For every candidate run `python3 scripts/tracker.py check "<name>"` and drop any that are featured.
6. Score each 1–10 on recency, stage fit (seed–B best), insight strength. Rank.

Write `pipeline/<week>/candidates.md`:

```
# Week <week> — Candidates
## Tuesday — AI for the D2C <role> (<angle>)
## Founder Friday
| # | Founder | Brand | Category | Trigger (date) | Stage | Insight angle | Score | Source |
## Brand Teardown — <category>
| # | Brand | Founders | Hero product (₹) | Why interesting | Score | Source |
## Needs the user
- Confirm founder is active on LinkedIn; pick 1 founder + 1 brand.
```

Every row needs a source URL. Never invent candidates to fill the table.
