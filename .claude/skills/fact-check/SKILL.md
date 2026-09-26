---
name: fact-check
description: Independently verify every claim in a LinkedIn draft against its fact sheet and sources before the user reviews it. Use after write-post, or when asked to "fact-check" a draft.
---

# Fact-check

Run in a **fresh subagent** (not the writer) so it checks the draft with no prior assumptions.

For each draft in `pipeline/<week>/drafts/`:
1. List every factual claim (numbers, dates, names, titles, funding, quotes, product details, tool capabilities).
2. Match each to a fact-sheet bullet and its source. Re-open the source URL for every number or quote.
3. Mark each: ✅ verified · ⚠️ softened/needs rewording · ❌ unsupported.
4. Check the guardrails: no criticism of tagged parties, no valuation/layoff speculation, spelling of names/brands, tags are all mentioned in the post.

Append to the draft:
```
## Fact-check
| Claim | Status | Source | Note |
```
Fix ❌ by removing or rewording the claim (never by adding an unsourced fact). Set `status: fact-checked` only when no ❌ remain.
