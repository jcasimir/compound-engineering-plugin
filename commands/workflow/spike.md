---
name: workflow:spike
description: Erin runs the full workflow autonomously — no feedback needed until she's done
argument-hint: "[what you want built]"
---

# Spike: Autonomous Workflow

Invoke Erin to run the entire workflow autonomously. She'll make all decisions herself and present you with the finished work.

<spike_goal> #$ARGUMENTS </spike_goal>

**If no goal was provided, stop and ask:** "What would you like me to spike? Give me a brief description and I'll take it from brainstorm through compound."

---

@agent-other-erin, you're running in **spike mode**. This means:

## Spike Rules

1. **Run autonomously** — Don't ask for user input. Make decisions yourself and keep moving.

2. **Default to simpler** — When choosing between approaches, pick the simpler one. YAGNI.

3. **Keep moving** — Complete all phases: brainstorm → plan → plan-review → code → code-review → compound. Don't stop between phases.

4. **Make decisions, document them** — Every decision you'd normally ask about, just make it. Note what you decided and why.

5. **Only stop for true blockers:**
   - Missing credentials or environment setup you can't resolve
   - Requirements so ambiguous they could go very wrong
   - Something that would be destructive or irreversible

6. **Skip lengthy reviews** — Run reviewers but don't iterate multiple rounds. Take their top findings, address critical ones, note the rest.

7. **Time-box yourself** — This is a spike, not a polished product. Get something working, not something perfect.

## Spike Goal

<goal>
#$ARGUMENTS
</goal>

## Execution

Run through all phases:

1. **Brainstorm** (brief) — Quick exploration, pick an approach, move on
2. **Plan** (minimal) — Create a focused plan, don't over-engineer
3. **Plan Review** (fast) — Run reviewers, address showstoppers only
4. **Code** — Build it
5. **Code Review** (fast) — Run reviewers, fix critical issues only
6. **Compound** — Document what you learned

## Output

When complete, present:

```markdown
## Spike Complete: [Title]

### What I Built
[Brief description of what was implemented]

### Key Decisions I Made
1. **[Decision]** — [Why I chose this]
2. **[Decision]** — [Why I chose this]

### Files Created/Modified
- `path/to/file` — [what it does]

### Review Findings (Deferred)
Issues noted but not addressed in this spike:
- [Finding] — [Why deferred]

### To Polish Later
If you want to take this from spike to production:
- [ ] [What needs work]

### Learnings Captured
- `docs/solutions/[path]` — [What was documented]

### Links
- Plan: `docs/plans/[path]`
- PR: [if created]
```

---

Now run the spike for the goal above. Keep moving, make decisions, and bring back the finished work.
