# Compounding Engineering Plugin

AI-powered development tools that get smarter with every use. Make each unit of engineering work easier than the last.

## Components

| Component | Count |
|-----------|-------|
| Agents | 36 |
| Commands | 26 |
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

This plugin provides 26 commands organized into categories. Core workflow commands use `workflows:` prefix to avoid collisions with Claude Code's built-in commands.

### Workflow Commands

The primary development workflow commands that form the backbone of the compounding engineering process. Commands are numbered to show the natural sequence:

| # | Command | Deep Variant | Description |
|---|---------|--------------|-------------|
| 0 | `/workflows:0-brainstorm` | — | Explore requirements and approaches through collaborative dialogue. Answers **WHAT** to build. |
| 1 | `/workflows:1-plan` | `/workflows:1-plan:deep` | Transform feature descriptions into well-structured markdown plans. Deep variant adds parallel research for each section. |
| 2 | `/workflows:2-plan-review` | `/workflows:2-plan-review:deep` | Have 8 specialized reviewers (product strategy + technical architecture) analyze a plan. Deep variant adds two-round cross-pollination. |
| 3 | `/workflows:3-code` | — | Execute work plans efficiently while maintaining quality. Takes a plan file and implements it systematically. |
| 4 | `/workflows:4-code-review` | `/workflows:4-code-review:deep` | Perform exhaustive code reviews using multi-agent analysis. Deep variant adds two-round collaborative review. |
| 5 | `/workflows:5-compound` | — | Document a recently solved problem. Creates structured docs in `docs/solutions/` with YAML frontmatter. |

### Parallel Resolution Commands

Commands that leverage parallel processing to resolve multiple items simultaneously:

| Command | Description |
|---------|-------------|
| `/resolve_parallel` | Find all TODO comments in the codebase, analyze dependencies, and resolve them using parallel sub-agents. Outputs a mermaid flow diagram showing execution order. |
| `/resolve_pr_parallel` | Get all unresolved PR comments and resolve them in parallel. Automatically detects current branch and associated PR context. |
| `/resolve_todo_parallel` | Resolve all pending CLI todos from the `todos/*.md` directory using parallel processing. Analyzes dependencies to determine optimal execution order. |

### Testing & QA Commands

Commands for testing, bug reproduction, and quality assurance:

| Command | Description |
|---------|-------------|
| `/test-browser` | Run end-to-end browser tests on pages affected by a PR or branch using agent-browser CLI. Supports PR number, branch name, or 'current' for current branch. |
| `/reproduce-bug` | Investigate a GitHub issue by reading the description, running parallel log investigation agents (Rails console, Appsignal), and analyzing potential failure points. |
| `/xcode-test` | Build and test iOS apps on simulator using XcodeBuildMCP. Captures screenshots, logs, and verifies app behavior. |

### Documentation Commands

Commands for generating and maintaining documentation:

| Command | Description |
|---------|-------------|
| `/changelog` | Create engaging, witty changelogs for recent merges to main branch. Supports daily (24h) or weekly (7 days) summaries with developer credits. |
| `/release-docs` | Regenerate the documentation site to match current plugin components. Updates stats, reference pages, and validates counts. |
| `/deploy-docs` | Validate the documentation site and prepare it for GitHub Pages deployment. Runs component counts and JSON validation. |
| `/feature-video` | Record a video walkthrough demonstrating a feature using agent-browser, upload it, and embed it in the PR description. |

### Skill & Command Management

Commands for creating and fixing plugin components:

| Command | Description |
|---------|-------------|
| `/create-agent-skill` | Create or edit Claude Code skills with expert guidance on structure, frontmatter, and best practices. |
| `/generate_command` | Create a new custom slash command in `.claude/commands/` following conventions. Understands file operations, search, and editing capabilities. |
| `/heal-skill` | Fix incorrect SKILL.md files when a skill has wrong instructions or outdated API references. Analyzes conversation context to detect issues. |

### Issue Management Commands

Commands for triaging and reporting issues:

| Command | Description |
|---------|-------------|
| `/triage` | Go through findings one by one and decide whether to add each to the CLI todo system. For processing code review findings, security audits, or performance analysis. Does NOT write code—triage only. |
| `/report-bug` | Report a bug in the compound-engineering plugin. Gathers structured information and creates a GitHub issue for the maintainer. |

### Automation Commands

Commands for full autonomous workflows:

| Command | Description |
|---------|-------------|
| `/lfg` | Full autonomous engineering workflow. Runs 1-plan → 1-plan:deep → 3-code → 4-code-review → resolve todos → test-browser → feature-video in sequence. |
| `/agent-native-audit` | Comprehensive review against agent-native architecture principles (Action Parity, Tools as Primitives, Context Injection, etc.) with scored report. |

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
# Add the marketplace
claude /plugin marketplace add https://github.com/jcasimir/compound-engineering-plugin

# Install the plugin
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
