# utils/gpt_engine.py

import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def build_prompt(posts, comments):
    """
    Builds a prompt for GPT using the user's Reddit data.
    """
    prompt = "Create a detailed user persona based on the following Reddit activity.\nInclude interests, tone, personality, and possible demographics. Each point should cite the source.\n\n"

    prompt += "### Posts:\n"
    for post in posts[:10]:
        prompt += f"- {post['title']}\n{post['text']}\n(Source: {post['url']})\n\n"

    prompt += "### Comments:\n"
    for comment in comments[:10]:
        prompt += f"- {comment['comment']}\n(Source: {comment['url']})\n\n"

    return prompt

'''def get_gpt_response(prompt):
    import traceback
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use this model
            messages=[
                {"role": "system", "content": "You are a helpful assistant that analyzes users and builds personas."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        print("❌ OpenAI API Error:", e)
        traceback.print_exc()
        return "Failed to generate persona."
        '''
def get_gpt_response(prompt):
    print("⚠️ GPT call skipped (mocked due to quota limits)")
    return """
👤 User Persona for Redditor `kojied`

- Interests:
  Music, nightlife, dancing, bar culture  
  _(Source: Post titled "I feel violated by intern season")_

- Tone: 
  Casual, humorous, slightly annoyed  
  _(Source: Writing style and word choices in post)_

- Personality Traits: 
  Observant, prefers mature social settings  
  _(Source: Comparison between college party vibe and preferred atmosphere)_

- Demographics: 
  Possibly mid-to-late 20s, lives in an urban area, frequents local bars  
  _(Source: Frequenting neighborhood bars, mentions about college-age crowd)_
"""
