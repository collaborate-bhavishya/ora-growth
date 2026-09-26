# ora-growth — LinkedIn content system for Indian D2C

Three weekly posts (Tue AI for the D2C ___, Wed Brand Teardown, Fri Founder Friday), researched and drafted by Claude, approved by a human, scheduled via Buffer.

- Strategy & guardrails: `strategy/strategy.md` — read before any content work.
- Voice: `strategy/voice-guide.md` + `strategy/voice-samples.md`.
- Templates: `templates/`. State: `data/` (only change via `scripts/tracker.py`).
- Skills: `weekly-run` orchestrates `scout` → `research` → `write-post` → `fact-check`; `schedule-buffer` only after explicit approval.
- Weekly output: `pipeline/<YYYY>-W<ww>/{candidates.md,factsheets/,drafts/}`.

Hard rules: every fact sourced (URL + date); never estimate numbers; never schedule/publish without the user's approval; linkedin.com is not reachable — ask the user to paste posts.

Tests: `cd scripts && python3 -m unittest test_tracker`.
