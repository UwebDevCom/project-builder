#!/usr/bin/env python3
"""
Post-commit hook runner.
Receives commit metadata and appends structured knowledge entries
to the daily log and COMMIT_INDEX.md.

Usage (called by scripts/post-commit.sh or post-commit.bat):
  python scripts/mine-commit.py \
    --hash <sha> --author <name> --message <msg> \
    --stat <stat> --diff <diff> --date <YYYY-MM-DD>
"""
import argparse
from datetime import date
from pathlib import Path

# Anchor knowledge/ to the plugin root (this file lives in <plugin>/scripts/),
# not to the runtime cwd — the post-commit hook may run from anywhere.
PLUGIN_ROOT = Path(__file__).resolve().parent.parent
KNOWLEDGE_DIR = PLUGIN_ROOT / "knowledge"
DAILY_DIR = KNOWLEDGE_DIR / "daily"
COMMITS_DIR = KNOWLEDGE_DIR / "commits"

SKIP_WORDS = {"prettier", "lint", "format", "bump", "merge", "whitespace", "typo", "reformat"}


def should_skip(message: str, stat: str) -> bool:
    words = set(message.lower().split())
    if words & SKIP_WORDS:
        return True
    # Count total lines changed from stat summary line
    # e.g. "3 files changed, 12 insertions(+), 2 deletions(-)"
    total = 0
    for token in stat.split():
        if token.isdigit():
            total += int(token)
    return total < 5


def classify(message: str) -> str:
    msg = message.lower()
    if any(w in msg for w in ("fix", "bug", "error", "crash", "patch", "revert")):
        return "fix"
    if any(w in msg for w in ("refactor", "clean", "rename", "move", "reorganize")):
        return "refactor"
    if any(w in msg for w in ("decide", "switch", "migrate", "replace", "adopt", "drop")):
        return "decision"
    return "feature"


def build_entry(args) -> str:
    return (
        f"\n### [{args.hash[:8]}] {args.date} — {args.author}\n"
        f"**Message:** {args.message}\n"
        f"**Changed:** {args.stat.strip() or 'N/A'}\n"
        f"**Knowledge:** _Pending compiler-agent analysis_\n"
        f"**Type:** {classify(args.message)}\n"
    )


def append_to_daily(entry: str, log_date: str) -> None:
    DAILY_DIR.mkdir(parents=True, exist_ok=True)
    log = DAILY_DIR / f"{log_date}.md"
    is_new = not log.exists()
    with log.open("a", encoding="utf-8") as f:
        if is_new:
            f.write(f"# Daily Log — {log_date}\n\n## Commits\n")
        f.write(entry)


def append_to_index(entry: str) -> None:
    COMMITS_DIR.mkdir(parents=True, exist_ok=True)
    index = COMMITS_DIR / "COMMIT_INDEX.md"
    if not index.exists():
        index.write_text("# Commit Index\n\n", encoding="utf-8")
    with index.open("a", encoding="utf-8") as f:
        f.write(entry)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--hash", required=True)
    parser.add_argument("--author", required=True)
    parser.add_argument("--message", required=True)
    parser.add_argument("--stat", default="")
    parser.add_argument("--diff", default="")
    parser.add_argument("--date", default=str(date.today()))
    args = parser.parse_args()

    if should_skip(args.message, args.stat):
        print(f"[mine-commit] Skipped {args.hash[:8]} (trivial commit)")
        return

    entry = build_entry(args)
    append_to_daily(entry, args.date)
    append_to_index(entry)
    print(f"[mine-commit] Logged {args.hash[:8]} ({classify(args.message)}) to daily log + COMMIT_INDEX")


if __name__ == "__main__":
    main()
