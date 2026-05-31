#!/usr/bin/env python3
"""
SessionStart hook — injects project knowledge into Claude's context.
Reads INDEX.md (master catalog) and the last 2 daily logs, then
prints them wrapped in XML tags so Claude Code picks them up automatically.

Registered in hooks/hooks.json under "SessionStart".
"""
from datetime import date, timedelta
from pathlib import Path

# Anchor knowledge/ to the plugin root (this file lives in <plugin>/scripts/),
# not to the runtime cwd — hooks may run from any directory.
PLUGIN_ROOT = Path(__file__).resolve().parent.parent
KNOWLEDGE_DIR = PLUGIN_ROOT / "knowledge"
MAX_INDEX_LINES = 200
MAX_DAILY_LINES = 100


def read_capped(path: Path, max_lines: int) -> str:
    if not path.exists():
        return ""
    lines = path.read_text(encoding="utf-8").splitlines()
    truncated = lines[:max_lines]
    result = "\n".join(truncated)
    if len(lines) > max_lines:
        result += f"\n\n_[Truncated — {len(lines) - max_lines} more lines. Run /kb-search for full retrieval.]_"
    return result


def main() -> None:
    parts = []

    index_path = KNOWLEDGE_DIR / "INDEX.md"
    index_content = read_capped(index_path, MAX_INDEX_LINES)
    if index_content:
        parts.append(f"<knowledge-index>\n{index_content}\n</knowledge-index>")

    daily_dir = KNOWLEDGE_DIR / "daily"
    for i in range(2):
        day = date.today() - timedelta(days=i)
        log_path = daily_dir / f"{day}.md"
        content = read_capped(log_path, MAX_DAILY_LINES)
        if content:
            label = "today" if i == 0 else "yesterday"
            parts.append(f"<daily-log date='{day}' ({label})>\n{content}\n</daily-log>")

    if parts:
        print("\n\n".join(parts))
    # If knowledge/ doesn't exist yet, print nothing — no error, just silent


if __name__ == "__main__":
    main()
