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

**You MUST invoke each workflow phase using the Skill tool.** Don't do the work yourself — use the workflow commands, which invoke the specialized agents and reviewers.

1. **Brainstorm** — Invoke `/workflow:0-brainstorm` with the goal. When it asks for user input, you decide.
2. **Plan** — Invoke `/workflow:1-plan` with what you learned. When it asks for input, you decide.
3. **Plan Review** — Invoke `/workflow:2-plan-review` with the plan path. Take reviewer findings, address critical ones, note the rest.
4. **Code** — Invoke `/workflow:3-code` with the plan. Build it.
5. **Code Review** — Invoke `/workflow:4-code-review`. Take reviewer findings, fix critical issues only.
6. **Compound** — Invoke `/workflow:5-compound`. Document what you learned.

**Critical:** Each phase invokes specialized agents and reviewers. That's the whole point of the workflow. Don't bypass them by doing everything inline.

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
