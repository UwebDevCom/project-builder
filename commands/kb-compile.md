---
description: Run the compiler agent to promote daily logs into concept articles
---

Steps:
1. Check `knowledge/log.md` to find the timestamp of the last compile run.
2. List all daily logs in `knowledge/daily/` modified after that timestamp.
3. If none found: "Knowledge base is up to date. No new logs to compile."
4. If logs found: spawn the **compiler-agent** with the list of unprocessed files.
5. When complete, display the compiler's summary (articles created, updated, logs processed).
6. End with: "Run /kb-status to see the full knowledge base state."
