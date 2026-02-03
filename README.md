# jcasimir-plugins

A Claude Code plugin marketplace featuring the **Compound Engineering Plugin** — tools that make each unit of engineering work easier than the last.

## Philosophy

**Each unit of engineering work should make subsequent units easier—not harder.**

Traditional development accumulates technical debt. Every feature adds complexity. The codebase becomes harder to work with over time.

Compound engineering inverts this. 80% is in planning and review, 20% is in execution:
- Plan thoroughly before writing code
- Review to catch issues and capture learnings
- Codify knowledge so it's reusable
- Keep quality high so future changes are easy

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

## Profiles

Two teams of reviewers guide your work through planning and implementation.

### Plan Reviewers (Phase 2)

These reviewers evaluate your plans before you write code, helping you think through scope, strategy, and approach.

| Name | Inspired By | What I Bring |
|------|-------------|--------------|
| [Avi](https://en.wikipedia.org/wiki/Avi_Flombaum) | Avi Flombaum, Flatiron School | Rails conventions exist for good reasons. I look for what's next while respecting what works. |
| [Charles](https://en.wikipedia.org/wiki/Charles_Eames) | Charles Eames, designer | The details aren't details — they're the design. I ask what problem you're really solving and whether your constraints are creative gifts. |
| [Greg](https://gregbaugues.com/) | Greg Baugues, Twilio | I've spent two years deep in AI tools. I know what they actually do well versus the hype. |
| [Jason](https://en.wikipedia.org/wiki/Jason_Fried) | Jason Fried, 37signals | I cut scope for a living. Show me a plan, and I'll show you what can wait. Sustainable pace beats heroic effort. |
| [Marty](https://www.svpg.com/team/marty-cagan/) | Marty Cagan, SVPG | Have you validated this? I push teams past assumptions to evidence. Discovery before delivery. |
| [Melissa](https://melissaperri.com/) | Melissa Perri, author | I spot build traps — when you're shipping features without outcomes. Connect your plan to what customers actually need. |
| [Sandy](https://en.wikipedia.org/wiki/Sandy_Speicher) | Sandy Speicher, IDEO | Who's affected by this plan? I advocate for the humans at the margins — the ones most often overlooked. |
| [Steve](https://stevekinney.net/) | Steve Kinney, Frontend Masters | I teach because clarity is everything. If your frontend can't be explained simply, it's too complex. |

### Code Reviewers (Phase 4)

These reviewers analyze your implementation, each bringing a specialized lens to catch issues and improve quality.

| Name | Inspired By | What I Bring |
|------|-------------|--------------|
| Abby | Project manager | I synthesize the team's expertise into clear priorities. Review isn't about mistakes — it's about building toward excellence. |
| Alex | Startup veteran | I find joy in deleting code. Every line removed can't break, can't confuse, doesn't need maintenance. |
| Corey | Hourglass testing advocate | I'm skeptical of vanity coverage. Acceptance tests at the top, domain tests at the bottom — and be pragmatic about sad paths. |
| Donna | Quiet data guardian | I don't make noise about every little thing. But when data is at risk, everyone hears me. |
| [Florence](https://en.wikipedia.org/wiki/Florence_Griffith_Joyner) | Florence Griffith-Joyner | Every millisecond matters. Your users shouldn't wait for slow software. |
| [Jim](https://en.wikipedia.org/wiki/Jim_Weirich) | Jim Weirich, Rake creator | Version control is storytelling. Every commit is a message to your past, present, and future selves. |
| Julik | Race condition hunter | Timing is everything. I hunt race conditions in JavaScript because janky UIs are the first sign of cheap software. |
| Kevin | Reformed black hat | I spent my youth breaking into systems. Now I use that knowledge to find the holes before someone else does. |
| [Maya](https://en.wikipedia.org/wiki/Maya_Lin) | Maya Lin, architect | I see software like an architect sees buildings — structures that must bear weight and endure time. |
| Robo | Futurist | I'm building for tomorrow. If an agent can't do what a user can, we're not ready for the future. |
| [Sandi](https://sandimetz.com/) | Sandi Metz, author | I see patterns where others see lines of code. I'll even pull up external resources mid-review to verify best practices. |

## Learn More

- [Full component reference](plugins/compound-engineering/README.md) - all agents, commands, skills
- [OpenCode/Codex support](docs/opencode-codex.md) - experimental conversion to other formats
- [Compound engineering: how Every codes with agents](https://every.to/chain-of-thought/compound-engineering-how-every-codes-with-agents)
- [The story behind compounding engineering](https://every.to/source-code/my-ai-had-already-fixed-the-code-before-i-saw-it)
