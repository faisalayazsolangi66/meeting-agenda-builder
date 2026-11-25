# Meeting Agenda Builder

Build a formatted meeting agenda from bullet points, with numbered items
and time slots.

## Requirements

- Python 3 (standard library only)

## How to run

```bash
python3 main.py "Welcome and introductions" "Project status update" "Next steps"
```

Options:

- `-f, --file FILE` — read one item per line from a text file
- `-t, --title TITLE` — agenda title (default: `Meeting Agenda`)
- `-d, --date DATE` — meeting date, e.g. `2026-11-26` (default: today)
- `--start HH:MM` — start time (default: `10:00`)
- `--minutes N` — minutes per item (default: `10`)
- `-o, --output FILE` — write the agenda to a file instead of printing it

## Example

```bash
python3 main.py --title "Weekly Standup" --start 09:30 --minutes 15 \
  "Welcome" "Sprint review" "Blockers" "Next steps"
```

Sample output:

```
Weekly Standup
==============
Date: 2026-11-25

1. 09:30 - 09:45  Welcome
2. 09:45 - 10:00  Sprint review
3. 10:00 - 10:15  Blockers
4. 10:15 - 10:30  Next steps

Total: 4 item(s), 60 minutes.
```

## License

MIT — see [LICENSE](LICENSE).
