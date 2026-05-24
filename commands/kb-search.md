---
description: Search the project knowledge base using the retrieval agent
argument-hint: <query, e.g. "auth flow" or "why did we switch databases">
---

Search project knowledge for: "$ARGUMENTS"

Steps:
1. Spawn the **retrieval-agent** with the query: "$ARGUMENTS"
2. Return the agent's summary verbatim — do not paraphrase.
3. If confidence is low, suggest running `/kb-compile` to process recent daily logs.

If $ARGUMENTS is empty, ask the user what they want to find.
