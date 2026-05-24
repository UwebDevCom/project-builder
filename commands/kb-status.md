---
description: Show the health and coverage of the project knowledge base
---

Steps:
1. Read `knowledge/INDEX.md` — count articles by category.
2. Read `knowledge/log.md` — find last compile timestamp.
3. List `knowledge/daily/` — count logs processed vs. pending.
4. Check `knowledge/commits/COMMIT_INDEX.md` — count mined commits.

Display:

```
## Knowledge Base Status

| Category      | Articles |
|---------------|----------|
| Concepts      | N        |
| Connections   | N        |
| Commits mined | N        |
| Q&A           | N        |

Last compiled: YYYY-MM-DD HH:MM
Pending daily logs: N (run /kb-compile to process)

Coverage: <estimate — e.g. "3 weeks of sessions">
Retrieval strategy: <Index-guided | Index + FTS5 | Hybrid BM25+vector>
```

5. If pending logs > 3, add: "Warning: knowledge base is stale. Run /kb-compile."
6. End with: "Run /kb-search <query> to retrieve knowledge, or /kb-compile to update."
