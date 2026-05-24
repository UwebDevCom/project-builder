---
description: >
  Mine a git commit for team knowledge. Auto-triggers from post-commit hook or when
  user says "mine this commit", "what did this commit change", "why was X changed".
  Extracts decisions, patterns, and rationale from commit messages and diffs.
---

# Commit Mining Protocol

## What to extract from every commit

- **Why** (from commit message + diff context): rationale for the change
- **What pattern**: new patterns or conventions introduced
- **What broke first**: if a fix commit, what was the root cause
- **Files that matter**: which modules are evolving fast (hotspots)
- **Decision signals**: comments like `// switched from X to Y because`

## What to skip

- Formatting-only commits (prettier, lint, whitespace fixes)
- Dependency bumps with no logic changes
- Merge commits
- Commits with fewer than 5 lines changed

## Output format

Append to `knowledge/commits/COMMIT_INDEX.md`:

```markdown
### [hash] [date] — [author]
**Message:** [commit message]
**Changed:** [key files — list up to 5]
**Knowledge:**
- [fact 1 — one sentence]
- [fact 2 — one sentence]
- [fact 3 — one sentence, omit if nothing more]
**Type:** fix | feature | refactor | decision
```

Also append under `## Commits` in today's `knowledge/daily/YYYY-MM-DD.md`.

## Hotspot tracking

If the same file appears in 3+ consecutive commits, note it in `knowledge/concepts/hotspots.md`:
```
- `path/to/file` — N commits in last 30 days. Reason: <infer from messages>
```
