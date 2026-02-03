# Imagegen Plugin

AI image generation with style presets and multi-image support. Powered by Google Gemini.

## Install

```bash
/plugin install https://github.com/jcasimir/compound-engineering-plugin?plugin=imagegen
```

## Setup

Set your Gemini API key:

```bash
export GEMINI_API_KEY="your-api-key-here"
```

Create the Python environment:

```bash
python3 -m venv ~/.gemini-venv
~/.gemini-venv/bin/pip install google-genai Pillow
```

## Quick Start

```bash
/imagegen "A mountain sunset" sunset.jpg
```

## Features

- **Text-to-image**: Generate images from natural language prompts
- **Image editing**: Modify existing images with natural language
- **Style presets**: 23 built-in styles (anime, photorealistic, cinematic, etc.)
- **Multiple variations**: Generate up to 4 images at once
- **Flexible sizing**: Multiple aspect ratios and resolutions (1K, 2K, 4K)

## Style Presets

| Category | Styles |
|----------|--------|
| Photography | `photorealistic`, `portrait`, `product`, `street`, `cinematic`, `aerial` |
| Art | `anime`, `watercolor`, `oil-painting`, `sketch`, `comic`, `pixel-art`, `3d-render` |
| Era/Aesthetic | `80s-retro`, `90s-vintage`, `minimalist`, `maximalist`, `vaporwave` |
| Technical | `blueprint`, `infographic`, `ui-mockup` |
| Mood | `dark-moody`, `bright-airy`, `golden-hour` |

## Examples

```bash
# Basic generation
/imagegen "A coffee shop" shop.jpg

# With style preset
/imagegen "A city street" street.jpg --style cinematic

# Multiple variations
/imagegen "A logo" logo.jpg --count 4 --style minimalist

# High resolution
/imagegen "Epic landscape" landscape.jpg --aspect 16:9 --size 2K
```

## Available Scripts

| Script | Purpose |
|--------|---------|
| `generate_image.py` | Text-to-image generation |
| `edit_image.py` | Edit existing images with prompts |
| `compose_images.py` | Combine multiple reference images |
| `multi_turn_chat.py` | Iterative refinement via chat |

## Use Cases

- App icons and illustrations
- Product photography mockups
- UI design assets
- Marketing visuals
- Concept art and storyboards
- Logo exploration
