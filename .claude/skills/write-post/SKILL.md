---
name: write-post
description: Turn a fact sheet into a LinkedIn draft using the series template and voice guide. Use after research, or when asked to "write", "draft" or "redo" a post for Founder Friday, Brand Teardown or AI for the D2C ___.
---

# Write post

Read first: `strategy/voice-guide.md`, `strategy/voice-samples.md` (match it if filled), the series template in `templates/`, and the fact sheet.

Output `pipeline/<week>/drafts/<day>-<series-slug>.md`:

```
---
series: Founder Friday | Brand Teardown | AI for the D2C <role>
publish_at: <YYYY-MM-DD>T08:45:00+05:30
status: draft            # draft → fact-checked → approved → scheduled
tags_buffer: [<company pages to tag via Buffer>]
tags_manual: [<people to tag by hand on LinkedIn>]
visual: <what image/card to attach>
first_comment: <source links>
---
## Hook A
## Hook B
## Post
<full post using Hook A>
## Carousel (AI series only)
```

Rules:
- Only use facts in the fact sheet. If you need a fact that isn't there, stop and send it back to research.
- Two hooks that differ in approach (number-led vs contrast/story).
- Follow word limits, emoji cap, hashtags and banned list from the voice guide.
- No links in the post body.
