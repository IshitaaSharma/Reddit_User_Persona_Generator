# utils/reddit_scraper.py

import praw
from dotenv import load_dotenv
import os

load_dotenv()

# 🔐 Use Reddit credentials from your .env
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

def extract_username_from_url(url):
    """
    Extracts Reddit username from profile URL.
    e.g. https://www.reddit.com/user/kojied/ → kojied
    """
    return url.strip("/").split("/")[-1]

def fetch_user_data(username, limit=50):
    """
    Fetches user's posts and comments from Reddit.
    """
    try:
        redditor = reddit.redditor(username)
        posts = []
        comments = []

        for submission in redditor.submissions.new(limit=limit):
            posts.append({
                "title": submission.title,
                "text": submission.selftext,
                "url": f"https://www.reddit.com{submission.permalink}"
            })

        for comment in redditor.comments.new(limit=limit):
            comments.append({
                "comment": comment.body,
                "url": f"https://www.reddit.com{comment.permalink}"
            })

        return posts, comments

    except Exception as e:
        print(f"❌ Error fetching data: {e}")
        return [], []
