# Compound Engineering Plugin

## Directory Structure

```
agents/       # Flat folder, agents prefixed by workflow phase or "other-"
commands/     # Slash commands (workflows/ for numbered sequence)
skills/       # Skills with SKILL.md files
```

## Agent Naming Convention

Agents are named by workflow phase prefix:
- `0-brainstorm-*.md` — Research agents for exploration (Phase 0)
- `1-plan-*.md` — Research agents for planning (Phase 1)
- `2-plan-review-*.md` — Plan reviewers (Phase 2)
- `3-code-*.md` — Design sync, linting, bug reproduction (Phase 3)
- `4-code-review-*.md` — Code reviewers (Phase 4)
- `5-compound-*.md` — Process review, documentation (Phase 5)
- `other-*.md` — On-demand utilities (pr-comment-resolver, git-history-analyzer)

## Workflow Commands

Numbered sequence: 0-brainstorm → 1-plan → 2-plan-review → 3-code → 4-code-review → 5-compound

## Adding Components

### Agents

Add `.md` file to `agents/` with appropriate prefix and frontmatter:

```yaml
---
name: {phase}-{agent-name}   # e.g., 2-plan-review-jason-fried, 4-code-review-corey-test
description: "When to use this agent. Include <example> blocks showing context, user message, assistant response, and <commentary>."
model: inherit
---
```

If adding a **reviewer**, also add a row to README.md Profiles table:

```markdown
| [Name](wikipedia-or-site-link) | Role (2-4 words) | First-person "What I Bring" statement |
```

### Commands

Add `.md` file to `commands/` (or `commands/workflows/` for workflow commands):

```yaml
---
name: command-name
description: One-line description
argument-hint: "[what argument to pass]"
---
```

### Skills

Add directory to `skills/` containing `SKILL.md` with frontmatter:

```yaml
---
name: skill-name
description: "This skill should be used when..." (third person)
---
```
