---
name: grill-me
description: >
  Relentless interview that stress-tests a plan against the project's domain model,
  sharpens terminology, and updates documentation inline as decisions crystallise.
  Use when the user wants to pressure-test a plan, a feature design, or an architecture decision.
---

<what-to-do>

Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one. For each question, provide your recommended answer.

Ask the questions one at a time, waiting for feedback on each question before continuing.

If a question can be answered by exploring the codebase or existing docs, explore them instead of asking.

</what-to-do>

<supporting-info>

## Domain awareness

Before the first question, scan for existing documentation:

### File structure

```
assets/
├── docs/
│   ├── CONTEXT.md          ← glossary of canonical project terms
│   └── adr/
│       ├── 0001-*.md       ← architecture decision records
│       └── 0002-*.md
├── design/
│   └── *.png / *.jpg       ← screenshots and mockups (read these visually)
└── plans/
    └── *.md                ← feature plans, PRDs, spike notes
```

Create files lazily — only when you have something to write.
If `assets/docs/CONTEXT.md` doesn't exist, create it when the first term is resolved.
If `assets/docs/adr/` doesn't exist, create it when the first ADR is warranted.

Also check the project root for a `CONTEXT.md` or `CONTEXT-MAP.md` — some projects keep it there.

## During the session

### Challenge against the glossary

When the user uses a term that conflicts with language in `assets/docs/CONTEXT.md`, call it out immediately.
"Your glossary defines 'cancellation' as X, but you seem to mean Y — which is it?"

### Sharpen fuzzy language

When the user uses vague or overloaded terms, propose a precise canonical term.
"You're saying 'account' — do you mean the Customer or the User? Those are different things."

### Read design assets

If screenshots or mockups exist in `assets/design/`, read them before questioning.
When the user's verbal description contradicts what's shown in a design file, surface it:
"Your mockup shows a single confirm button, but you're describing a two-step flow — which is correct?"

### Cross-reference with plans

If plans or PRDs exist in `assets/plans/`, check them for prior decisions before asking.
Avoid re-asking questions already answered in a plan doc.

### Discuss concrete scenarios

Stress-test domain relationships with specific edge cases.
Force the user to be precise about concept boundaries before moving on.

### Cross-reference with code

When the user states how something works, check whether the code agrees.
If you find a contradiction, surface it: "Your code does X, but you just said Y — which is right?"

### Update CONTEXT.md inline

When a term is resolved, write it to `assets/docs/CONTEXT.md` immediately.
Don't batch — capture decisions as they happen.

`CONTEXT.md` is a glossary only. No implementation details, no specs, no scratch notes.

Format:
```markdown
# Project Glossary

## <Term>
<One-sentence definition. What it is, not how it works.>
```

### Offer ADRs sparingly

Only create an ADR in `assets/docs/adr/` when all three are true:

1. **Hard to reverse** — the cost of changing your mind later is meaningful
2. **Surprising without context** — a future reader will wonder "why did they do it this way?"
3. **The result of a real trade-off** — there were genuine alternatives and you chose one for specific reasons

If any of the three is missing, skip the ADR.

ADR format (`assets/docs/adr/NNNN-<slug>.md`):
```markdown
# NNNN — <Title>

**Date:** YYYY-MM-DD
**Status:** accepted

## Context
<What problem forced a decision?>

## Decision
<What was decided, in one sentence.>

## Consequences
<What becomes easier. What becomes harder.>

## Alternatives considered
- <Option A> — rejected because <reason>
- <Option B> — rejected because <reason>
```

</supporting-info>
