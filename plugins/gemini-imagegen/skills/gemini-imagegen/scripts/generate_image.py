#!/usr/bin/env python3
"""
Generate images from text prompts using Gemini API.

Usage:
    python generate_image.py "prompt" output.jpg [--model MODEL] [--aspect RATIO] [--size SIZE]
    python generate_image.py "prompt" output.jpg --count 4
    python generate_image.py "prompt" output.jpg --style photorealistic

Examples:
    python generate_image.py "A cat in space" cat.jpg
    python generate_image.py "A logo for Acme Corp" logo.jpg --aspect 1:1
    python generate_image.py "Epic landscape" landscape.jpg --aspect 16:9 --size 2K
    python generate_image.py "A coffee shop" shop.jpg --style anime --count 3
    python generate_image.py "Product photo of sneakers" shoes.jpg --style product

Environment:
    GEMINI_API_KEY - Required API key
"""

import argparse
import os
import sys
from pathlib import Path

from google import genai
from google.genai import types


# Style presets - prompt suffixes that produce consistent aesthetics
STYLE_PRESETS = {
    # Photography styles
    "photorealistic": "photorealistic, 85mm lens, natural lighting, high detail, sharp focus",
    "portrait": "professional portrait photography, 85mm f/1.4, shallow depth of field, studio lighting, catchlights in eyes",
    "product": "professional product photography, studio lighting, white background, commercial quality, high detail",
    "street": "street photography style, candid, natural light, 35mm lens, urban environment",
    "cinematic": "cinematic still, anamorphic lens, film grain, dramatic lighting, movie scene",
    "aerial": "aerial drone photography, bird's eye view, landscape, high altitude perspective",

    # Art styles
    "anime": "anime style, cel shading, vibrant colors, clean lines, Japanese animation aesthetic",
    "watercolor": "watercolor painting, soft edges, visible brushstrokes, artistic, traditional media look",
    "oil-painting": "oil painting style, rich colors, visible brushwork, classical art technique",
    "sketch": "pencil sketch, hand-drawn, graphite on paper, artistic linework, shading",
    "comic": "comic book style, bold outlines, dynamic composition, halftone dots, superhero aesthetic",
    "pixel-art": "pixel art style, 16-bit aesthetic, retro gaming, crisp pixels, limited color palette",
    "3d-render": "3D rendered, Pixar style, smooth surfaces, global illumination, CGI quality",

    # Era/aesthetic styles
    "80s-retro": "1980s aesthetic, neon colors, synthwave, retro-futuristic, VHS quality",
    "90s-vintage": "1990s style, vintage film photography, nostalgic, muted colors",
    "minimalist": "minimalist design, clean, simple, lots of white space, modern aesthetic",
    "maximalist": "maximalist style, busy, detailed, ornate, rich patterns and colors",
    "vaporwave": "vaporwave aesthetic, pink and cyan, Greek statues, retro computer graphics, surreal",

    # Technical styles
    "blueprint": "technical blueprint, white lines on blue background, engineering diagram, schematic",
    "infographic": "infographic style, clean data visualization, icons, clear typography, informative",
    "ui-mockup": "UI mockup, clean interface design, modern app aesthetic, flat design",

    # Mood/atmosphere
    "dark-moody": "dark and moody, dramatic shadows, low key lighting, mysterious atmosphere",
    "bright-airy": "bright and airy, high key lighting, soft shadows, optimistic mood",
    "golden-hour": "golden hour lighting, warm tones, sunset atmosphere, magical light",
}


def generate_images(
    prompt: str,
    output_path: str,
    model: str = "gemini-2.5-flash-image",
    aspect_ratio: str | None = None,
    image_size: str | None = None,
    count: int = 1,
    style: str | None = None,
) -> list[tuple[str, str | None]]:
    """Generate one or more images from a text prompt.

    Args:
        prompt: Text description of the image to generate
        output_path: Path to save the generated image(s)
        model: Gemini model to use
        aspect_ratio: Aspect ratio (1:1, 16:9, 9:16, etc.)
        image_size: Resolution (1K, 2K, 4K - 4K only for pro model)
        count: Number of images to generate (1-4)
        style: Style preset name to apply

    Returns:
        List of (output_path, text_response) tuples for each generated image
    """
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise EnvironmentError("GEMINI_API_KEY environment variable not set")

    # Apply style preset to prompt
    if style:
        if style not in STYLE_PRESETS:
            available = ", ".join(sorted(STYLE_PRESETS.keys()))
            raise ValueError(f"Unknown style '{style}'. Available: {available}")
        prompt = f"{prompt}, {STYLE_PRESETS[style]}"

    client = genai.Client(api_key=api_key)

    # Build config
    config_kwargs = {"response_modalities": ["TEXT", "IMAGE"]}

    image_config_kwargs = {}
    if aspect_ratio:
        image_config_kwargs["aspect_ratio"] = aspect_ratio
    if image_size:
        image_config_kwargs["image_size"] = image_size

    if image_config_kwargs:
        config_kwargs["image_config"] = types.ImageConfig(**image_config_kwargs)

    config = types.GenerateContentConfig(**config_kwargs)

    # Prepare output paths
    output = Path(output_path)
    stem = output.stem
    suffix = output.suffix or ".jpg"
    parent = output.parent

    results = []

    # Generate images (multiple API calls if count > 1)
    for i in range(count):
        response = client.models.generate_content(
            model=model,
            contents=[prompt],
            config=config,
        )

        text_response = None
        for part in response.parts:
            if part.text is not None:
                text_response = part.text
            elif part.inline_data is not None:
                image = part.as_image()

                # Generate output filename
                if count == 1:
                    img_path = output_path
                else:
                    img_path = str(parent / f"{stem}_{i + 1}{suffix}")

                image.save(img_path)
                results.append((img_path, text_response))

    if not results:
        raise RuntimeError("No images were generated. Check your prompt and try again.")

    return results


def list_styles():
    """Print available style presets."""
    print("Available style presets:\n")

    # Group by category
    categories = {
        "Photography": ["photorealistic", "portrait", "product", "street", "cinematic", "aerial"],
        "Art": ["anime", "watercolor", "oil-painting", "sketch", "comic", "pixel-art", "3d-render"],
        "Era/Aesthetic": ["80s-retro", "90s-vintage", "minimalist", "maximalist", "vaporwave"],
        "Technical": ["blueprint", "infographic", "ui-mockup"],
        "Mood": ["dark-moody", "bright-airy", "golden-hour"],
    }

    for category, styles in categories.items():
        print(f"{category}:")
        for style in styles:
            desc = STYLE_PRESETS[style][:60] + "..." if len(STYLE_PRESETS[style]) > 60 else STYLE_PRESETS[style]
            print(f"  {style:15} - {desc}")
        print()


def main():
    parser = argparse.ArgumentParser(
        description="Generate images from text prompts using Gemini API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument("prompt", nargs="?", help="Text prompt describing the image")
    parser.add_argument("output", nargs="?", help="Output file path (e.g., output.jpg)")
    parser.add_argument(
        "--model", "-m",
        default="gemini-2.5-flash-image",
        choices=["gemini-2.5-flash-image", "gemini-3-pro-image-preview"],
        help="Model to use (default: gemini-2.5-flash-image)"
    )
    parser.add_argument(
        "--aspect", "-a",
        choices=["1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"],
        help="Aspect ratio"
    )
    parser.add_argument(
        "--size", "-s",
        choices=["1K", "2K", "4K"],
        help="Image resolution (4K only available with pro model)"
    )
    parser.add_argument(
        "--count", "-c",
        type=int,
        choices=[1, 2, 3, 4],
        default=1,
        help="Number of images to generate (1-4, default: 1)"
    )
    parser.add_argument(
        "--style",
        help="Style preset to apply (use --list-styles to see options)"
    )
    parser.add_argument(
        "--list-styles",
        action="store_true",
        help="List available style presets and exit"
    )

    args = parser.parse_args()

    # Handle --list-styles
    if args.list_styles:
        list_styles()
        return

    # Validate required args
    if not args.prompt or not args.output:
        parser.error("prompt and output are required (unless using --list-styles)")

    try:
        results = generate_images(
            prompt=args.prompt,
            output_path=args.output,
            model=args.model,
            aspect_ratio=args.aspect,
            image_size=args.size,
            count=args.count,
            style=args.style,
        )

        for path, text in results:
            print(f"Image saved to: {path}")
            if text:
                print(f"Model response: {text}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
