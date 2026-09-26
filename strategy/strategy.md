# LinkedIn Content Strategy — Indian D2C

**Promise:** The place Indian D2C builders come to see who's winning, what they're building, and how AI is changing their jobs.

**Audience:** founders, marketers and operators at Indian D2C brands.

## Weekly rhythm (3 posts, 8:30–9:30 am IST)

| Day | Series | Pillar | Format |
|---|---|---|---|
| Tuesday | AI for the D2C ___ | AI × Roles (flagship) | Carousel (6–8 slides) or long text |
| Wednesday | Brand Teardown | D2C brands | Text + 1 product/brand image |
| Friday | Founder Friday | Founders | Text + clean card (name, brand, milestone) |

Review the mix after 6 weeks using Buffer metrics.

## Series

### Founder Friday
Eligibility (Scout scores on these):
- Trigger in the last 30 days: funding, revenue/GMV milestone, new category or offline expansion, Shark Tank India, notable launch.
- Seed to Series B (much more likely to engage than unicorn founders).
- Active on LinkedIn in the last 30 days (best reshare predictor) — confirmed manually, since Claude can't read LinkedIn.
- Not featured in the last 90 days (`scripts/tracker.py check`).

### Brand Teardown
Category rotation lives in `data/categories.json`. Positive or neutral analysis only — never criticise a brand you tag.

### AI for the D2C ___
8 roles × 4 angles in `data/topic-bank.json` (32 posts ≈ 8 months of Tuesdays). A timely news hook (e.g. new Meta/Google/Shopify/Amazon AI feature) may override the next topic.

## Tagging & amplification
- Buffer can reliably tag **company pages**; personal-profile tagging via API is likely unsupported — add founder tags manually on LinkedIn right after publishing.
- Optional DM to the featured founder: "Featured you in today's Founder Friday — thought you'd like to see it."
- Reply to every comment in the first hour.

## Guardrails
- Human approval for every post. Nothing auto-publishes.
- Every number/claim needs a source dated within 90 days. No source → cut. Never estimate revenue.
- No speculation on layoffs, valuations, down-rounds. No criticism of tagged people/brands.
- No founder photos without permission — use logos, product images or a designed card.
- 90-day cool-off before re-featuring a person or brand.

## Measurement (monthly, via Buffer `get_aggregated_post_metrics`)
Impressions & engagement rate per series · reshares by tagged people · ICP comments · follower growth · inbound DMs.
