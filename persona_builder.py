# utils/persona_builder.py

def save_persona_to_file(username, persona_text):
    """
    Saves the GPT-generated persona to a text file.
    """
    filename = f"{username}_persona.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(persona_text)
    print(f"✅ Persona saved to: {filename}")
