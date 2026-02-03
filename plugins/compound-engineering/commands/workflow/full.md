---
name: workflow:full
description: Start a project with Erin as your project manager — she'll guide you through the full workflow
argument-hint: "[what you want to build or improve]"
---

# Start a Project with Erin

Invoke Erin (@agent-other-erin) to manage your project from start to finish.

<project_goal> #$ARGUMENTS </project_goal>

Erin will:
1. Understand what you're trying to build
2. Assess the scope and complexity
3. Guide you through the appropriate workflow steps
4. Ensure nothing gets skipped
5. Capture learnings at the end

**Workflow she manages:**
```
0-brainstorm → 1-plan → 2-plan-review → 3-code → 4-code-review → 5-compound
```

She's pragmatic — not everything needs every step. Quick fixes skip to coding. Clear features skip brainstorming. But significant work gets the full treatment.

@agent-other-erin, a user wants to start a project. Here's what they want to build:

<goal>
#$ARGUMENTS
</goal>

If no goal was provided, ask them: "What would you like to build or improve today?"

Then assess the scope and guide them through the appropriate workflow, starting with the right phase for this type of work.
