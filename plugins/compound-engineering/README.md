# Compounding Engineering Plugin

AI-powered development tools that get smarter with every use. Make each unit of engineering work easier than the last.

## Components

| Component | Count |
|-----------|-------|
| Agents | 36 |
| Commands | 25 |
| Skills | 15 |
| MCP Servers | 1 |

## Agents

Agents are organized into categories for easier discovery.

### Review (22)

All review agents have names and personalities to make feedback more engaging and memorable.

| Agent | Name | Description |
|-------|------|-------------|
| `abby-review-synthesis` | Abby | PM who synthesizes findings, respects each reviewer's expertise |
| `agent-native-reviewer` | Robo | Futurist ensuring features work for AI agents, not just humans |
| `architecture-strategist` | Maya | Systems thinker who sees structure like an architect sees buildings |
| `code-simplicity-reviewer` | Alex | Startup veteran who knows over-engineering kills projects |
| `corey-test-reviewer` | Corey | Hourglass testing advocate, pragmatic about sad paths |
| `data-integrity-guardian` | Donna | Quiet guardian who speaks up when data is at risk |
| `data-migration-expert` | Dana | Reserved specialist, meticulous about migration safety |
| `deployment-verification-agent` | Nathan | Trusted ops person who makes deploys boring and safe |
| `charles-eames-plan-reviewer` | Charles | Legendary designer, systems thinker, constraints as creative gifts |
| `jason-fried-plan-reviewer` | Jason | 37signals founder, champion of scope restraint and sustainability |
| `marty-cagan-plan-reviewer` | Marty | SVPG founder, discovery advocate, product risk assessor |
| `melissa-perri-plan-reviewer` | Melissa | Escapes build traps, outcomes over output champion |
| `sandy-speicher-plan-reviewer` | Sandy | Former IDEO CEO, human-centered design and equity advocate |
| `erin-process-reviewer` | Erin | Process guardian, ensures we learn from each cycle |
| `jim-git-reviewer` | Jim | Git as storytelling (tribute to Jim Weirich) |
| `julik-frontend-races-reviewer` | Julik | Spots race conditions in JavaScript and Stimulus code |
| `avi-rails-architect` | Avi | Rails technical architect, always looking for what's next |
| `greg-ai-reviewer` | Greg | AI pragmatist, reviews AI usage in dev and products |
| `steve-frontend-architect` | Steve | Frontend architect, simplifies complex UIs, performance-focused |
| `pattern-recognition-specialist` | Sandi | Deep thinker who researches patterns and best practices |
| `performance-oracle` | Florence | Flo-Jo believes in raw speed — every millisecond matters |
| `security-sentinel` | Kevin | Reformed black hat who thinks like an attacker |

### Research (5)

| Agent | Description |
|-------|-------------|
| `best-practices-researcher` | Gather external best practices and examples |
| `framework-docs-researcher` | Research framework documentation and best practices |
| `git-history-analyzer` | Analyze git history and code evolution |
| `learnings-researcher` | Search institutional learnings in docs/solutions/ for relevant past solutions |
| `repo-research-analyst` | Research repository structure and conventions |

### Design (3)

| Agent | Description |
|-------|-------------|
| `design-implementation-reviewer` | Verify UI implementations match Figma designs |
| `design-iterator` | Iteratively refine UI through systematic design iterations |
| `figma-design-sync` | Synchronize web implementations with Figma designs |

### Workflow (5)

| Agent | Description |
|-------|-------------|
| `bug-reproduction-validator` | Systematically reproduce and validate bug reports |
| `every-style-editor` | Edit content to conform to Every's style guide |
| `lint` | Run linting and code quality checks on Ruby and ERB files |
| `pr-comment-resolver` | Address PR comments and implement fixes |
| `spec-flow-analyzer` | Analyze user flows and identify gaps in specifications |

### Docs (1)

| Agent | Description |
|-------|-------------|
| `ankane-readme-writer` | Create READMEs following Ankane-style template for Ruby gems |

## Commands

### Workflow Commands

Core workflow commands use `workflows:` prefix to avoid collisions with built-in commands:

| Command | Description |
|---------|-------------|
| `/workflows:brainstorm` | Explore requirements and approaches before planning |
| `/workflows:plan` | Create implementation plans |
| `/workflows:review` | Run comprehensive code reviews |
| `/workflows:review-deep` | Two-round collaborative review where reviewers learn from each other |
| `/workflows:work` | Execute work items systematically |
| `/workflows:compound` | Document solved problems to compound team knowledge |

### Utility Commands

| Command | Description |
|---------|-------------|
| `/deepen-plan` | Enhance plans with parallel research agents for each section |
| `/changelog` | Create engaging changelogs for recent merges |
| `/create-agent-skill` | Create or edit Claude Code skills |
| `/generate_command` | Generate new slash commands |
| `/heal-skill` | Fix skill documentation issues |
| `/plan_review` | Multi-agent plan review in parallel |
| `/report-bug` | Report a bug in the plugin |
| `/reproduce-bug` | Reproduce bugs using logs and console |
| `/resolve_parallel` | Resolve TODO comments in parallel |
| `/resolve_pr_parallel` | Resolve PR comments in parallel |
| `/resolve_todo_parallel` | Resolve todos in parallel |
| `/triage` | Triage and prioritize issues |
| `/test-browser` | Run browser tests on PR-affected pages |
| `/xcode-test` | Build and test iOS apps on simulator |
| `/feature-video` | Record video walkthroughs and add to PR description |

## Skills

### Architecture & Design

| Skill | Description |
|-------|-------------|
| `agent-native-architecture` | Build AI agents using prompt-native architecture |

### Development Tools

| Skill | Description |
|-------|-------------|
| `andrew-kane-gem-writer` | Write Ruby gems following Andrew Kane's patterns |
| `compound-docs` | Capture solved problems as categorized documentation |
| `create-agent-skills` | Expert guidance for creating Claude Code skills |
| `dhh-rails-style` | Write Ruby/Rails code in DHH's 37signals style |
| `dspy-ruby` | Build type-safe LLM applications with DSPy.rb |
| `frontend-design` | Create production-grade frontend interfaces |
| `skill-creator` | Guide for creating effective Claude Code skills |

### Content & Workflow

| Skill | Description |
|-------|-------------|
| `every-style-editor` | Review copy for Every's style guide compliance |
| `file-todos` | File-based todo tracking system |
| `git-worktree` | Manage Git worktrees for parallel development |

### File Transfer

| Skill | Description |
|-------|-------------|
| `rclone` | Upload files to S3, Cloudflare R2, Backblaze B2, and cloud storage |

### Browser Automation

| Skill | Description |
|-------|-------------|
| `agent-browser` | CLI-based browser automation using Vercel's agent-browser |

### Image Generation

| Skill | Description |
|-------|-------------|
| `gemini-imagegen` | Generate and edit images using Google's Gemini API |

**gemini-imagegen features:**
- Text-to-image generation
- Image editing and manipulation
- Multi-turn refinement
- Multiple reference image composition (up to 14 images)

**Requirements:**
- `GEMINI_API_KEY` environment variable
- Python packages: `google-genai`, `pillow`

## MCP Servers

| Server | Description |
|--------|-------------|
| `context7` | Framework documentation lookup via Context7 |

### Context7

**Tools provided:**
- `resolve-library-id` - Find library ID for a framework/package
- `get-library-docs` - Get documentation for a specific library

Supports 100+ frameworks including Rails, React, Next.js, Vue, Django, Laravel, and more.

MCP servers start automatically when the plugin is enabled.

## Browser Automation

This plugin uses **agent-browser CLI** for browser automation tasks. Install it globally:

```bash
npm install -g agent-browser
agent-browser install  # Downloads Chromium
```

The `agent-browser` skill provides comprehensive documentation on usage.

## Installation

```bash
claude /plugin install compound-engineering
```

## Known Issues

### MCP Servers Not Auto-Loading

**Issue:** The bundled Context7 MCP server may not load automatically when the plugin is installed.

**Workaround:** Manually add it to your project's `.claude/settings.json`:

```json
{
  "mcpServers": {
    "context7": {
      "type": "http",
      "url": "https://mcp.context7.com/mcp"
    }
  }
}
```

Or add it globally in `~/.claude/settings.json` for all projects.

## Version History

See [CHANGELOG.md](CHANGELOG.md) for detailed version history.

## License

MIT
