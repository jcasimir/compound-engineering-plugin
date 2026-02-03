# Gemini Image Generation Plugin

Generate and edit images using Google's Gemini API.

## Requirements

- `GEMINI_API_KEY` environment variable must be set
- Python 3.10+ with venv at `~/.gemini-venv`

## Setup (One-Time)

```bash
python3 -m venv ~/.gemini-venv
~/.gemini-venv/bin/pip install google-genai Pillow
```

## Available Skills

### gemini-imagegen

Generate images from text prompts with style presets and multi-image support.

**Invoke with:** `/gemini-imagegen` or describe an image generation task

**Key Features:**
- Text-to-image generation
- Image editing with natural language
- 23 style presets (anime, photorealistic, cinematic, etc.)
- Generate up to 4 variations at once
- Multiple aspect ratios and resolutions

**Quick Examples:**
```bash
# Basic generation
generate_image.py "A mountain sunset" sunset.jpg

# With style preset
generate_image.py "A coffee shop" shop.jpg --style anime

# Multiple variations
generate_image.py "A logo" logo.jpg --count 4 --style minimalist
```

## When to Use This Plugin

- Creating mockups or concept images
- Generating app icons or illustrations
- Product photography mockups
- UI design assets
- Marketing visuals
- Any text-to-image task
