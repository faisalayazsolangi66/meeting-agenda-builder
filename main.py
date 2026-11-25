#!/usr/bin/env python3
"""Build a meeting agenda from bullet points.

Reads bullet points from the command line or a text file and prints a
nicely formatted agenda with numbered items and time slots.
"""
import argparse
import sys
from datetime import datetime, timedelta


def parse_args():
    p = argparse.ArgumentParser(
        description="Build a meeting agenda from bullet points.")
    p.add_argument("items", nargs="*", help="Agenda items (bullet points).")
    p.add_argument("-f", "--file", help="Text file with one item per line.")
    p.add_argument("-t", "--title", default="Meeting Agenda",
                   help="Agenda title (default: %(default)s).")
    p.add_argument("-d", "--date", default=None,
                   help="Meeting date, e.g. 2026-11-26 (default: today).")
    p.add_argument("--start", default="10:00",
                   help="Start time HH:MM (default: %(default)s).")
    p.add_argument("--minutes", type=int, default=10,
                   help="Minutes per item (default: %(default)s).")
    p.add_argument("-o", "--output", help="Write the agenda to this file.")
    return p.parse_args()


def load_items(args):
    items = list(args.items)
    if args.file:
        try:
            with open(args.file, encoding="utf-8") as fh:
                items += [line.strip(" \t\n-*\u2022") for line in fh]
        except OSError as exc:
            print(f"Error: cannot read {args.file}: {exc}", file=sys.stderr)
            sys.exit(1)
    items = [item for item in items if item]
    if not items:
        print("Error: no agenda items given. Pass items on the command line "
              "or with --file.", file=sys.stderr)
        sys.exit(1)
    return items


def build_agenda(title, date, start, minutes_each, items):
    try:
        current = datetime.strptime(start, "%H:%M")
    except ValueError:
        print(f"Error: start time must be HH:MM, got {start!r}.",
              file=sys.stderr)
        sys.exit(1)
    lines = [title, "=" * len(title), f"Date: {date}", ""]
    for i, item in enumerate(items, 1):
        end = current + timedelta(minutes=minutes_each)
        lines.append(f"{i}. {current.strftime('%H:%M')} - "
                     f"{end.strftime('%H:%M')}  {item}")
        current = end
    lines.append("")
    lines.append(f"Total: {len(items)} item(s), "
                 f"{len(items) * minutes_each} minutes.")
    return "\n".join(lines) + "\n"


def main():
    args = parse_args()
    items = load_items(args)
    date = args.date or datetime.now().strftime("%Y-%m-%d")
    agenda = build_agenda(args.title, date, args.start, args.minutes, items)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as fh:
            fh.write(agenda)
        print(f"Agenda written to {args.output}")
    else:
        print(agenda, end="")


if __name__ == "__main__":
    main()
