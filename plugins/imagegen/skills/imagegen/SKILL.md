---
name: imagegen
description: AI image generation from text prompts. Use for creating images, icons, mockups, illustrations, logos, and any visual content. Supports style presets (anime, photorealistic, cinematic, etc.), multiple variations, aspect ratios, and image editing. Powered by Google Gemini.
---

# Image Generation

Generate and edit images using Google's Gemini API. The environment variable `GEMINI_API_KEY` must be set.

## Setup (One-Time)

Create a Python virtual environment with required dependencies:

```bash
# Create venv (use a persistent location)
python3 -m venv ~/.gemini-venv

# Install dependencies
~/.gemini-venv/bin/pip install google-genai Pillow
```

Ensure `GEMINI_API_KEY` is set in your shell profile (`~/.zshrc` or `~/.bashrc`):

```bash
export GEMINI_API_KEY="your-api-key-here"
```

## Quick Start - Use the Scripts

This skill includes ready-to-use scripts in the `scripts/` directory. **Always use these instead of writing code from scratch.**

First, find the scripts directory:
```bash
SCRIPTS_DIR="${CLAUDE_PLUGIN_ROOT}/skills/imagegen/scripts"
```

### Generate an Image

```bash
~/.gemini-venv/bin/python "$SCRIPTS_DIR/generate_image.py" "A soccer ball on grass" output.jpg
```

Options:
- `--model` / `-m`: Model to use (`gemini-2.5-flash-image` default, or `gemini-3-pro-image-preview`)
- `--aspect` / `-a`: Aspect ratio (`1:1`, `16:9`, `9:16`, etc.)
- `--size` / `-s`: Resolution (`1K`, `2K`, `4K`)
- `--count` / `-c`: Generate multiple variations (1-4)
- `--style`: Apply a style preset (use `--list-styles` to see options)
- `--list-styles`: Show all available style presets

Example with options:
```bash
~/.gemini-venv/bin/python "$SCRIPTS_DIR/generate_image.py" \
  "Epic mountain landscape at sunset" \
  landscape.jpg \
  --aspect 16:9 \
  --size 2K
```

### Generate Multiple Variations

```bash
~/.gemini-venv/bin/python "$SCRIPTS_DIR/generate_image.py" \
  "A logo for a coffee shop" \
  logo.jpg \
  --count 4
# Outputs: logo_1.jpg, logo_2.jpg, logo_3.jpg, logo_4.jpg
```

### Apply Style Presets

Style presets append curated prompt suffixes for consistent aesthetics:

```bash
# List all available styles
~/.gemini-venv/bin/python "$SCRIPTS_DIR/generate_image.py" --list-styles

# Generate with a style
~/.gemini-venv/bin/python "$SCRIPTS_DIR/generate_image.py" \
  "A city street" \
  street.jpg \
  --style cinematic

# Combine style with multiple outputs
~/.gemini-venv/bin/python "$SCRIPTS_DIR/generate_image.py" \
  "A soccer player" \
  player.jpg \
  --style anime \
  --count 3
```

**Available Style Categories:**
- **Photography:** `photorealistic`, `portrait`, `product`, `street`, `cinematic`, `aerial`
- **Art:** `anime`, `watercolor`, `oil-painting`, `sketch`, `comic`, `pixel-art`, `3d-render`
- **Era/Aesthetic:** `80s-retro`, `90s-vintage`, `minimalist`, `maximalist`, `vaporwave`
- **Technical:** `blueprint`, `infographic`, `ui-mockup`
- **Mood:** `dark-moody`, `bright-airy`, `golden-hour`

### Edit an Existing Image

```bash
~/.gemini-venv/bin/python "$SCRIPTS_DIR/edit_image.py" \
  input.jpg \
  "Add a rainbow to the sky" \
  output.jpg
```

### Compose Multiple Images

```bash
~/.gemini-venv/bin/python "$SCRIPTS_DIR/compose_images.py" \
  "Create a collage of these photos" \
  output.jpg \
  photo1.jpg photo2.jpg photo3.jpg
```

### Multi-Turn Refinement (Interactive)

```bash
~/.gemini-venv/bin/python "$SCRIPTS_DIR/multi_turn_chat.py" output.jpg
# Then enter prompts interactively to refine the image
```

## Available Scripts

| Script | Purpose |
|--------|---------|
| `generate_image.py` | Text-to-image generation |
| `edit_image.py` | Edit existing images with prompts |
| `compose_images.py` | Combine multiple reference images |
| `multi_turn_chat.py` | Iterative refinement via chat |
| `gemini_images.py` | Full-featured CLI with all options |

## Models

| Model | Best For | Notes |
|-------|----------|-------|
| `gemini-2.5-flash-image` | Fast generation (default) | Works on free tier |
| `gemini-2.0-flash-exp-image-generation` | Experimental features | Works on free tier |
| `gemini-3-pro-image-preview` | Higher quality, 4K support | May require billing enabled |

## Quick Reference

### Available Aspect Ratios
`1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9`

### Available Resolutions
`1K` (default), `2K`, `4K` (4K requires pro model)

---

## API Reference (Advanced)

For custom implementations, here are the API patterns:

## Core API Pattern

```python
import os
from google import genai
from google.genai import types

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# Basic generation (1K, 1:1 - defaults)
response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents=["Your prompt here"],
    config=types.GenerateContentConfig(
        response_modalities=['TEXT', 'IMAGE'],
    ),
)

for part in response.parts:
    if part.text:
        print(part.text)
    elif part.inline_data:
        image = part.as_image()
        image.save("output.png")
```

## Custom Resolution & Aspect Ratio

```python
from google.genai import types

response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents=[prompt],
    config=types.GenerateContentConfig(
        response_modalities=['TEXT', 'IMAGE'],
        image_config=types.ImageConfig(
            aspect_ratio="16:9",  # Wide format
            image_size="2K"       # Higher resolution
        ),
    )
)
```

### Resolution Examples

```python
# 1K (default) - Fast, good for previews
image_config=types.ImageConfig(image_size="1K")

# 2K - Balanced quality/speed
image_config=types.ImageConfig(image_size="2K")

# 4K - Maximum quality, slower
image_config=types.ImageConfig(image_size="4K")
```

### Aspect Ratio Examples

```python
# Square (default)
image_config=types.ImageConfig(aspect_ratio="1:1")

# Landscape wide
image_config=types.ImageConfig(aspect_ratio="16:9")

# Ultra-wide panoramic
image_config=types.ImageConfig(aspect_ratio="21:9")

# Portrait
image_config=types.ImageConfig(aspect_ratio="9:16")

# Photo standard
image_config=types.ImageConfig(aspect_ratio="4:3")
```

## Editing Images

Pass existing images with text prompts:

```python
from PIL import Image

img = Image.open("input.png")
response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents=["Add a sunset to this scene", img],
    config=types.GenerateContentConfig(
        response_modalities=['TEXT', 'IMAGE'],
    ),
)
```

## Multi-Turn Refinement

Use chat for iterative editing:

```python
from google.genai import types

chat = client.chats.create(
    model="gemini-3-pro-image-preview",
    config=types.GenerateContentConfig(response_modalities=['TEXT', 'IMAGE'])
)

response = chat.send_message("Create a logo for 'Acme Corp'")
# Save first image...

response = chat.send_message("Make the text bolder and add a blue gradient")
# Save refined image...
```

## Prompting Best Practices

### Photorealistic Scenes
Include camera details: lens type, lighting, angle, mood.
> "A photorealistic close-up portrait, 85mm lens, soft golden hour light, shallow depth of field"

### Stylized Art
Specify style explicitly:
> "A kawaii-style sticker of a happy red panda, bold outlines, cel-shading, white background"

### Text in Images
Be explicit about font style and placement:
> "Create a logo with text 'Daily Grind' in clean sans-serif, black and white, coffee bean motif"

### Product Mockups
Describe lighting setup and surface:
> "Studio-lit product photo on polished concrete, three-point softbox setup, 45-degree angle"

## Advanced Features

### Google Search Grounding
Generate images based on real-time data:

```python
response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents=["Visualize today's weather in Tokyo as an infographic"],
    config=types.GenerateContentConfig(
        response_modalities=['TEXT', 'IMAGE'],
        tools=[{"google_search": {}}]
    )
)
```

### Multiple Reference Images (Up to 14)
Combine elements from multiple sources:

```python
response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents=[
        "Create a group photo of these people in an office",
        Image.open("person1.png"),
        Image.open("person2.png"),
        Image.open("person3.png"),
    ],
    config=types.GenerateContentConfig(
        response_modalities=['TEXT', 'IMAGE'],
    ),
)
```

## Important: File Format & Media Type

**CRITICAL:** The Gemini API returns images in JPEG format by default. When saving, always use `.jpg` extension to avoid media type mismatches.

```python
# CORRECT - Use .jpg extension (Gemini returns JPEG)
image.save("output.jpg")

# WRONG - Will cause "Image does not match media type" errors
image.save("output.png")  # Creates JPEG with PNG extension!
```

### Converting to PNG (if needed)

If you specifically need PNG format:

```python
from PIL import Image

# Generate with Gemini
for part in response.parts:
    if part.inline_data:
        img = part.as_image()
        # Convert to PNG by saving with explicit format
        img.save("output.png", format="PNG")
```

### Verifying Image Format

Check actual format vs extension with the `file` command:

```bash
file image.png
# If output shows "JPEG image data" - rename to .jpg!
```

## Notes

- All generated images include SynthID watermarks
- Gemini returns **JPEG format by default** - always use `.jpg` extension
- Image-only mode (`responseModalities: ["IMAGE"]`) won't work with Google Search grounding
- For editing, describe changes conversationally—the model understands semantic masking
- Default to 1K resolution for speed; use 2K/4K when quality is critical
