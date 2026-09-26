---
name: weekly-run
description: Run the full weekly LinkedIn pipeline (scout → research → write → fact-check) and hand the user 3 drafts to review. Use when asked for "this week's posts", "weekly run", or by the scheduled routine.
---

# Weekly run

Posts go out Tue (AI for the D2C ___), Wed (Brand Teardown), Fri (Founder Friday), 8:45 am IST. Week = ISO week of the posts' Monday.

1. `scout` → `pipeline/<week>/candidates.md`.
2. If the user is present, ask them to pick 1 founder + 1 brand (show top 3 each). If running unattended, take the top-scored and say so.
3. `research` — three subagents in parallel (founder, brand, AI topic).
4. `write-post` × 3.
5. `fact-check` × 3 in fresh subagents.
6. Commit + push `pipeline/<week>/`.
7. Report to the user: 3 drafts (both hooks), any ⚠️ items, and what needs their input (LinkedIn activity check, voice edits, approval).
8. Stop. Scheduling happens only via `schedule-buffer` after approval.
