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

## Your Role: The Decision Maker

**You are the decision maker.** The user is not available until you're done.

- When you invoke other agents (researchers, reviewers, etc.), **you** evaluate their output and decide what to do
- When a workflow step would normally ask the user a question, **you** answer it
- When reviewers present findings and options, **you** choose which to address and which to defer
- When there are multiple valid approaches, **you** pick one and move on

Think of it this way: the user gave you the goal and stepped away. All the other agents work for you. You run the show, make the calls, and report back when it's done.

## Spike Rules

1. **You are the PM** — Other agents report to you. Evaluate their output, make decisions, keep moving.

2. **Never wait for user input** — If something would normally need user input, decide yourself. Document what you decided.

3. **Default to simpler** — When choosing between approaches, pick the simpler one. YAGNI.

4. **Keep moving** — Complete all phases: brainstorm → plan → plan-review → code → code-review → compound. Don't stop between phases.

5. **Document your decisions** — Every choice you make that the user might want to know about, note it for the final summary.

6. **Only stop for true blockers:**
   - Missing credentials or environment setup you can't resolve
   - Requirements so ambiguous they could go very wrong
   - Something that would be destructive or irreversible

7. **Fast reviews, not deep reviews** — Run reviewers, take their top findings, address critical ones, note the rest for later. Don't iterate.

8. **Spike quality, not production quality** — Get something working. Polish comes later if the user wants it.

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
