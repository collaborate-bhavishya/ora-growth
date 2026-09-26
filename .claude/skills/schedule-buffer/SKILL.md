---
name: schedule-buffer
description: Schedule approved LinkedIn drafts in Buffer and record them in the featured tracker. Use only when the user has approved specific drafts ("approve", "schedule", "send to Buffer").
---

# Schedule in Buffer

**Only schedule drafts the user explicitly approved in this conversation.** Nothing auto-publishes.

1. Buffer tools: `get_account` → confirm the organization by name with the user → `list_channels` → the LinkedIn channel. Record its id in `data/buffer.json` (`{"organization": ..., "linkedin_channel_id": ...}`) to reuse.
2. For each approved draft: `create_post` on the LinkedIn channel, text = `## Post` section (with the hook the user chose), scheduled at `publish_at`. Mention company pages if Buffer supports it for the channel; otherwise leave plain names.
3. Update front matter: `status: scheduled`, `buffer_post_id: <id>`.
4. Update state:
   - Founder: `python3 scripts/tracker.py add --name "<founder>" --type founder --series "Founder Friday" --week <week> --date <publish date>` (also the brand, `--type brand`).
   - Brand Teardown: `tracker.py add ... --type brand --series "Brand Teardown"` and `tracker.py use-category --category "<cat>" --week <week>`.
   - AI post: `tracker.py use-topic --role "<role>" --angle <angle> --week <week>`.
5. Commit and push the pipeline + data changes.
6. Tell the user the manual follow-up for each post: tags in `tags_manual`, visual to attach, first comment with sources, optional founder DM.
