---
description: Fetches a work item (task, ticket, or user story) from the project memory or MCP source
---

# Get Work Item

Retrieves a work item by ID or by the current active item.

## How to fetch

1. If an ID is provided (e.g. `WI-42`), search memory for that ID.
2. If no ID is given, retrieve the item tagged as `status:active`.
3. If neither exists, tell the caller: "No active work item found. Use /memory-save to store one."

## Work item format expected in memory

```
id: WI-<number>
title: <short title>
type: feature | bug | chore
status: active | done | blocked
description: <what needs to be built or fixed>
acceptance: <how we know it's done>
```

## Output

Return the work item as a structured object so the calling agent can use each field directly.
Do not summarize or paraphrase — return the raw fields.
