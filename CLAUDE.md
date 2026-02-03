# Compound Engineering Plugin

## Directory Structure

```
agents/       # Specialized review, research, design, workflow, docs agents
commands/     # Slash commands (workflows/ for numbered sequence)
skills/       # Skills with SKILL.md files
```

## Workflow Commands

Numbered sequence: 0-brainstorm → 1-plan → 2-plan-review → 3-code → 4-code-review → 5-compound

## Adding Components

### Agents

Add `.md` file to appropriate `agents/` subdirectory with frontmatter:

```yaml
---
name: agent-name
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
