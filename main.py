# main.py

from utils.reddit_scraper import extract_username_from_url, fetch_user_data
from utils.gpt_engine import build_prompt, get_gpt_response
from utils.persona_builder import save_persona_to_file
from utils.image_generator import generate_persona_image

def main():
    # 🔹 You will paste the Reddit profile URL here when prompted
    url = input("🔗 Enter Reddit profile URL: ").strip()
    
    # 🔹 Extract username from the URL (e.g., kojied from https://www.reddit.com/user/kojied/)
    username = extract_username_from_url(url)
    print(f"\n📥 Fetching data for: {username}...")

    # 🔹 Scrape posts and comments using the username
    posts, comments = fetch_user_data(username)
    if not posts and not comments:
        print("❌ No data found or user doesn't exist.")
        return

    print("🧠 Generating user persona...")

    # 🔹 Create GPT prompt and get response
    prompt = build_prompt(posts, comments)

    print("\n📤 Sending prompt to GPT...")
    print(prompt[:500])  # show a preview

    persona = get_gpt_response(prompt)

    print("\n📄 Final Output Preview:\n")
    print(persona[:500] + "...")  # Show preview

    # 🔹 Save full output to text file
    save_persona_to_file(username, persona)

    with open(f"{username}_persona.txt", "r", encoding="utf-8") as f:
        text = f.read()

    generate_persona_image(username, text, f"{username}_persona.png")

if __name__ == "__main__":
    main()
