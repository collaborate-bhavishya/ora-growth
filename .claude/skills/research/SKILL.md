---
name: research
description: Build a sourced fact sheet for a chosen founder, brand, or AI×role topic. Use after scout, when the user picks a candidate, or when asked to "research" a founder/brand/topic.
---

# Research

Output: `pipeline/<week>/factsheets/{founder,brand,ai-role}.md`. For independent targets, run the three in parallel subagents.

## Rules
- **Every claim is a bullet with source URL + publish date.** No source → not in the fact sheet.
- Numbers exactly as reported ("₹25 Cr", not "~₹25 Cr"). Never estimate revenue, valuation, or growth.
- Quotes verbatim with attribution.
- Flag conflicts between sources under `## Uncertain`.
- linkedin.com is blocked. If the user pasted a LinkedIn post, use it and cite "LinkedIn post pasted by user, <date>".

## Founder fact sheet
Founders & background · brand, category, founding year · product & price range · channels (D2C site, marketplaces, quick commerce, offline) · trigger (what/when/amount/investors) · reported metrics · quotes · **The insight** (what they did differently + evidence) · tag targets (company page, founder — LinkedIn URLs marked unverified) · Uncertain.

## Brand fact sheet
Hero product (what, price, differentiation) · positioning & customer · pricing logic · growth engine · funding & metrics · **One thing to steal** + evidence · tag targets · Uncertain.

## AI × role fact sheet
Relevant AI capabilities (official sources, dates) · adoption data (India preferred) · task table: task | today | with AI (tool/method) | human still owns · what not to trust AI with · India context (festive season, quick commerce, regional language) · Uncertain. Opinions allowed but labelled as opinion.
