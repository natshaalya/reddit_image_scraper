import praw
import json
import os
import requests
from dotenv import load_dotenv

# Load Reddit API credentials from .env
load_dotenv()
CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
USER_AGENT = "image_scraper:v1.0 (by u/yourusername)"

# Initialize Reddit instance
reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     user_agent=USER_AGENT)

# Choose subreddit
subreddit_name = "iphone"  # Change to any subreddit you like
subreddit = reddit.subreddit(subreddit_name)

# 10 pages * 25 posts ≈ 250 posts
posts = subreddit.hot(limit=250)

# Prepare folders
os.makedirs("downloads", exist_ok=True)

data = []

for post in posts:
    if post.url.endswith((".jpg", ".jpeg", ".png")):
        # Save metadata to JSON
        data.append({
            "title": post.title,
            "url": post.url,
            "subreddit": post.subreddit.display_name,
            "author": str(post.author),
            "upvotes": post.score,
            "created_utc": post.created_utc
        })

        # Download image
        try:
            response = requests.get(post.url)
            filename = os.path.join("downloads", post.url.split("/")[-1])
            with open(filename, "wb") as f:
                f.write(response.content)
        except Exception as e:
            print(f"Failed to download {post.url}: {e}")

# Save JSON metadata
with open(f"{subreddit_name}_images.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f"✅ Saved {len(data)} posts and downloaded images into 'downloads/' folder.")





