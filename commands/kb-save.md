---
description: Manually append a note to today's daily knowledge log
argument-hint: <note, e.g. "decided to use JWT over sessions because stateless scaling">
---

Save to today's knowledge log: "$ARGUMENTS"

Steps:
1. Open (or create) `knowledge/daily/YYYY-MM-DD.md` for today.
2. Append under a `## [HH:MM] Manual note` heading:
   ```
   - $ARGUMENTS
   ```
3. Confirm: "Saved to today's log. Run /kb-compile to promote this to a concept article."

If $ARGUMENTS is empty, ask what to save.
