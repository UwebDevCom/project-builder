---
description: Manually mine recent git commits into the knowledge base
argument-hint: <N — number of commits to mine, default 10>
---

Steps:
1. Determine N: use "$ARGUMENTS" as the count, or default to 10 if empty.
2. Run: `git log --oneline -N` to list the N most recent commits.
3. For each commit, run: `git show <hash> --stat` to get the diff stat.
4. Skip commits that match skip patterns (merge, prettier, lint, format, bump, whitespace, or < 5 lines changed).
5. For each kept commit, use the **commit-miner** skill to extract knowledge.
6. Append results to `knowledge/commits/COMMIT_INDEX.md` and today's daily log.
7. Report: "Mined N commits — M kept, P skipped (trivial). Run /kb-compile to promote to concept articles."

Note: This command is for manual recovery. The post-commit hook (scripts/post-commit.sh) should handle this automatically during normal workflow.
