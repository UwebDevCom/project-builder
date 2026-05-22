---
description: Knowledge base for the project — read and write structured facts via the memory API (brain.js)
---

# Memory Skill

Provides read/write access to the project's persistent knowledge base, backed by `brain.js`.

## Operations

### save(entry)
Store a new fact. Entry shape:
```js
{
  category: "architecture" | "requirement" | "convention" | "decision" | "work-item",
  key: "unique-slug",          // used for deduplication and lookup
  value: "the fact to store",
  tags: ["optional", "tags"]
}
```

### search(query)
Full-text search across all entries. Returns an array of matching entries sorted by relevance.

### get(key)
Exact lookup by slug. Returns null if not found.

### list(category?)
List all entries, optionally filtered by category.

### delete(key)
Remove an entry by slug.

## Notes

- All operations are performed through `brain.js` — do not read/write memory files directly.
- Keys must be kebab-case and unique within a category.
- If a `save` key already exists, the value is overwritten (upsert behavior).
