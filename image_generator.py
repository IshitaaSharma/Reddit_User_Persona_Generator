# utils/image_generator.py

from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

def generate_persona_image(username, persona_text, output_path):
    # Create blank canvas
    width, height = 1200, 1800
    background = (255, 255, 255)
    image = Image.new("RGB", (width, height), background)
    draw = ImageDraw.Draw(image)

    # Load fonts
    try:
        title_font = ImageFont.truetype("arialbd.ttf", 48)
        header_font = ImageFont.truetype("arialbd.ttf", 36)
        text_font = ImageFont.truetype("arial.ttf", 24)
    except:
        # Fallback if system fonts not found
        title_font = ImageFont.load_default()
        header_font = ImageFont.load_default()
        text_font = ImageFont.load_default()

    y = 50
    margin = 60

    # Draw Title
    draw.text((margin, y), f"User Persona: {username}", font=title_font, fill="black")
    y += 80

    # Split into sections
    sections = persona_text.strip().split("\n\n")
    for section in sections:
        if not section.strip():
            continue

        if ":" in section.split("\n")[0]:
            # Heading + Content
            lines = section.strip().split("\n")
            heading = lines[0].strip()
            draw.text((margin, y), heading, font=header_font, fill="darkorange")
            y += 40

            content = "\n".join(lines[1:])
        else:
            content = section.strip()

        # Wrap and draw text
        wrapped_text = textwrap.wrap(content, width=100)
        for line in wrapped_text:
            draw.text((margin, y), line, font=text_font, fill="black")
            y += 30
        y += 20  # extra spacing between sections

    # Save
    image.save(output_path)
    print(f"✅ Persona image saved to: {output_path}")
