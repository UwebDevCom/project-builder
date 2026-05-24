#!/usr/bin/env python3
"""
Stop / PreCompact hook trigger.
Appends a timestamped flush marker to today's daily log so the
compiler-agent knows a session ended and knowledge is ready to extract.

Usage:
  python scripts/flush.py --trigger session-end
  python scripts/flush.py --trigger pre-compact
"""
import argparse
from datetime import date, datetime
from pathlib import Path

KNOWLEDGE_DIR = Path("knowledge")
DAILY_DIR = KNOWLEDGE_DIR / "daily"


def get_today_log() -> Path:
    DAILY_DIR.mkdir(parents=True, exist_ok=True)
    return DAILY_DIR / f"{date.today()}.md"


def flush(trigger: str) -> None:
    log = get_today_log()
    is_new = not log.exists()
    timestamp = datetime.now().strftime("%H:%M")

    with log.open("a", encoding="utf-8") as f:
        if is_new:
            f.write(f"# Daily Log — {date.today()}\n\n")
        f.write(f"\n## [{timestamp}] Session flush ({trigger})\n")
        f.write("_Flush marker written. Run `/kb-compile` or wait for nightly compiler-agent._\n")

    print(f"[flush] Wrote flush marker to {log}  trigger={trigger}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flush session marker to daily knowledge log")
    parser.add_argument("--trigger", default="manual",
                        choices=["session-end", "pre-compact", "manual"],
                        help="What triggered the flush")
    args = parser.parse_args()
    flush(args.trigger)
