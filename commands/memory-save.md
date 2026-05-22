---
description: Save a piece of project knowledge to the memory knowledge base
argument-hint: <what to save, e.g. "the auth flow uses JWT with 24h expiry">
---

Save the following to project memory: "$ARGUMENTS"

Steps:
1. Use the memory skill to store the information.
2. Tag it appropriately (architecture, decision, requirement, convention, etc.).
3. Confirm to the user: "Saved to memory: <brief summary of what was stored>"

If $ARGUMENTS is empty, ask the user what they want to save before proceeding.
