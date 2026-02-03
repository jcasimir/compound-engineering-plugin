# Claude Code Plugin Marketplace

A collection of plugins for Claude Code.

## Install All Plugins

```bash
/plugin install https://github.com/jcasimir/compound-engineering-plugin
```

## Install Individual Plugins

```bash
# Compound Engineering - AI-powered development workflow
/plugin install https://github.com/jcasimir/compound-engineering-plugin?plugin=compound-engineering

# Imagegen - AI image generation
/plugin install https://github.com/jcasimir/compound-engineering-plugin?plugin=imagegen
```

## Available Plugins

### [Compound Engineering](./plugins/compound-engineering)

AI-powered development tools that get smarter with every use. Make each unit of engineering work easier than the last.

**Features:**
- Multi-agent plan review with 8 specialized reviewers
- Multi-agent code review with 14 specialized reviewers
- Workflow automation with Erin as project manager
- Knowledge compounding through documented learnings

**Quick Start:**
```bash
/workflow:full I want to build [your feature]
```

### [Imagegen](./plugins/imagegen)

AI image generation with style presets and multi-image support. Powered by Google Gemini.

**Features:**
- Text-to-image generation
- 23 style presets (anime, photorealistic, cinematic, etc.)
- Multiple variations (up to 4 at once)
- Image editing and composition

**Quick Start:**
```bash
/imagegen "A mountain sunset" sunset.jpg
```

## License

MIT
