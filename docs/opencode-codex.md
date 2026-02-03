# OpenCode + Codex Support (Experimental)

This repo includes a Bun/TypeScript CLI that converts Claude Code plugins to OpenCode and Codex formats.

## Installation

```bash
# Convert the compound-engineering plugin into OpenCode format
bunx @every-env/compound-plugin install compound-engineering --to opencode

# Convert to Codex format
bunx @every-env/compound-plugin install compound-engineering --to codex
```

## Local Development

```bash
bun run src/index.ts install ./plugins/compound-engineering --to opencode
```

## Output Locations

**OpenCode:** Written to `~/.opencode` by default, with `opencode.json` at the root and `agents/`, `skills/`, and `plugins/` alongside it.

**Codex:** Written to `~/.codex/prompts` and `~/.codex/skills`. Each Claude command is converted into both a prompt and a skill (the prompt instructs Codex to load the corresponding skill). Generated Codex skill descriptions are truncated to 1024 characters (Codex limit).

## Status

Both provider targets are experimental and may change as the formats evolve.
