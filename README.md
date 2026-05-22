# project-builder

A Claude Code plugin for planning, reviewing, and executing development work — from idea to shipped feature.

## What it does

| Command | Description |
|---------|-------------|
| `/memory-save <fact>` | Save a project fact to the knowledge base |
| `/memory-search <query>` | Search the knowledge base |
| `/memory-status` | Show everything stored in memory |

## Agents

| Agent | Trigger | What it does |
|-------|---------|--------------|
| `architect` | Planning a new feature | Reads design + PRD + work item → produces a step-by-step implementation plan |
| `design-reviewer` | Before implementation | Loads assets and requirements → reviews design for issues and gaps |
| `code-review` | After writing code | Reviews diff for correctness, simplicity, and security |
| `test-debug` | On failing tests or bugs | Traces root cause → proposes minimal fix + regression test |

## Setup

1. Place design screenshots in `assets/` — agents load them automatically.
2. Use `/memory-save` to store your PRD, architecture decisions, and conventions.
3. Use `/memory-save` to create work items (`id: WI-1, type: feature, ...`).
4. Run an agent when you need it.

## Folder structure

```
project-builder/
├── agents/          # Sub-agents invoked during planning and review
├── commands/        # Slash commands available in Claude Code
├── skills/          # Reusable logic loaded by agents and commands
│   ├── get-work-item/
│   ├── edit-work-item/
│   └── memory/      # Knowledge base (skill.md + brain.js)
├── hooks/           # Claude Code hooks (lifecycle scripts)
├── assets/          # Project screenshots and design files
├── mcp.json         # MCP server configuration
└── memory.json      # Generated at runtime — do not edit manually
```
