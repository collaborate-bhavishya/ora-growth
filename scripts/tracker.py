#!/usr/bin/env python3
"""Deterministic state helpers for the LinkedIn pipeline.

Keeps dedupe (90-day cool-off) and topic/category rotation out of the
model's hands so every run makes the same decision.

Usage:
  tracker.py check <name>                     exit 1 if featured within cool-off
  tracker.py add --name N --type founder|brand --series S --week W [--date YYYY-MM-DD]
  tracker.py next-topic                       next unused role × angle for Tuesday
  tracker.py use-topic --role R --angle A --week W
  tracker.py next-category                    next category for Brand Teardown
  tracker.py use-category --category C --week W
"""
import argparse
import json
import sys
from datetime import date, timedelta
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"


def _load(name):
    return json.loads((DATA / name).read_text())


def _save(name, obj):
    (DATA / name).write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


def _norm(s):
    return " ".join(s.lower().split())


def recent_match(name, today=None):
    """Return the featured entry for `name` inside the cool-off window, or None."""
    featured = _load("featured.json")
    today = today or date.today()
    cutoff = today - timedelta(days=featured["cooloff_days"])
    for e in featured["entries"]:
        if _norm(e["name"]) == _norm(name) and date.fromisoformat(e["date"]) >= cutoff:
            return e
    return None


def topic_order(bank):
    """Each week a new role; the angle advances after every full pass of roles."""
    roles, angles = bank["roles"], bank["angles"]
    return [(roles[i % len(roles)], angles[(i // len(roles)) % len(angles)])
            for i in range(len(roles) * len(angles))]


def next_topic():
    bank = _load("topic-bank.json")
    used = {(u["role"], u["angle"]) for u in bank["used"]}
    for role, angle in topic_order(bank):
        if (role, angle) not in used:
            return role, angle
    return None


def next_category():
    cats = _load("categories.json")
    return cats["rotation"][len(cats["used"]) % len(cats["rotation"])]


def main(argv=None):
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check")
    c.add_argument("name")
    a = sub.add_parser("add")
    a.add_argument("--name", required=True)
    a.add_argument("--type", choices=["founder", "brand"], required=True)
    a.add_argument("--series", required=True)
    a.add_argument("--week", required=True)
    a.add_argument("--date", default=date.today().isoformat())
    sub.add_parser("next-topic")
    ut = sub.add_parser("use-topic")
    ut.add_argument("--role", required=True)
    ut.add_argument("--angle", required=True)
    ut.add_argument("--week", required=True)
    sub.add_parser("next-category")
    uc = sub.add_parser("use-category")
    uc.add_argument("--category", required=True)
    uc.add_argument("--week", required=True)
    args = p.parse_args(argv)

    if args.cmd == "check":
        hit = recent_match(args.name)
        if hit:
            print(f"FEATURED {hit['date']} in {hit['series']} ({hit['week']}) — skip")
            return 1
        print("OK — not featured in cool-off window")
        return 0
    if args.cmd == "add":
        featured = _load("featured.json")
        featured["entries"].append({"name": args.name, "type": args.type,
                                    "series": args.series, "week": args.week,
                                    "date": args.date})
        _save("featured.json", featured)
        print(f"added {args.name}")
        return 0
    if args.cmd == "next-topic":
        t = next_topic()
        if not t:
            print("topic bank exhausted — add roles/angles")
            return 1
        print(f"{t[0]} | {t[1]}")
        return 0
    if args.cmd == "use-topic":
        bank = _load("topic-bank.json")
        if args.role not in bank["roles"] or args.angle not in bank["angles"]:
            print("unknown role or angle", file=sys.stderr)
            return 2
        bank["used"].append({"role": args.role, "angle": args.angle, "week": args.week})
        _save("topic-bank.json", bank)
        print(f"used {args.role} | {args.angle}")
        return 0
    if args.cmd == "next-category":
        print(next_category())
        return 0
    if args.cmd == "use-category":
        cats = _load("categories.json")
        if args.category not in cats["rotation"]:
            print("unknown category", file=sys.stderr)
            return 2
        cats["used"].append({"category": args.category, "week": args.week})
        _save("categories.json", cats)
        print(f"used {args.category}")
        return 0


if __name__ == "__main__":
    sys.exit(main())
