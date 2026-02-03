# jcasimir-plugins

A Claude Code plugin marketplace featuring the **Compound Engineering Plugin** — tools that make each unit of engineering work easier than the last.

## Install

```bash
# Add the marketplace
/plugin marketplace add https://github.com/jcasimir/compound-engineering-plugin

# Install the plugin
/plugin install compound-engineering
```

## Workflow

```
Brainstorm → Plan → Plan Review → Code → Code Review → Compound → Repeat
```

| # | Command | Purpose |
|---|---------|---------|
| 0 | `/workflows:0-brainstorm` | Explore requirements before planning |
| 1 | `/workflows:1-plan` | Turn feature ideas into detailed implementation plans |
| 2 | `/workflows:2-plan-review` | Multi-agent plan review before coding |
| 3 | `/workflows:3-code` | Execute plans with worktrees and task tracking |
| 4 | `/workflows:4-code-review` | Multi-agent code review before merging |
| 5 | `/workflows:5-compound` | Document learnings to make future work easier |

Each cycle compounds: plans inform future plans, reviews catch more issues, patterns get documented.

## Philosophy

**Each unit of engineering work should make subsequent units easier—not harder.**

Traditional development accumulates technical debt. Every feature adds complexity. The codebase becomes harder to work with over time.

Compound engineering inverts this. 80% is in planning and review, 20% is in execution:
- Plan thoroughly before writing code
- Review to catch issues and capture learnings
- Codify knowledge so it's reusable
- Keep quality high so future changes are easy

## Learn More

- [Full component reference](plugins/compound-engineering/README.md) - all agents, commands, skills
- [OpenCode/Codex support](docs/opencode-codex.md) - experimental conversion to other formats
- [Compound engineering: how Every codes with agents](https://every.to/chain-of-thought/compound-engineering-how-every-codes-with-agents)
- [The story behind compounding engineering](https://every.to/source-code/my-ai-had-already-fixed-the-code-before-i-saw-it)
