---
description: Creates or updates a work item in project memory
---

# Edit Work Item

Creates a new work item or updates an existing one in memory.

## Usage

Call with an object containing any of these fields:

```
id: WI-<number>          # omit to auto-assign next ID
title: <short title>
type: feature | bug | chore
status: active | done | blocked
description: <what needs to be built>
acceptance: <definition of done>
```

## Behavior

- **Create**: if no `id` is given, auto-increment from the highest existing WI number.
- **Update**: if `id` matches an existing item, merge the provided fields (do not overwrite fields not passed in).
- **Activate**: setting `status: active` automatically sets all other items to `status: backlog` (only one active item at a time).

## Output

Return the final saved work item with all fields, including the assigned ID.
Confirm: "Work item WI-<n> saved."
