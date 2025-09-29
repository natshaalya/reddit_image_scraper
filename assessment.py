import praw
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

print("DEBUG CLIENT_ID:", os.getenv("REDDIT_CLIENT_ID"))
print("DEBUG CLIENT_SECRET:", os.getenv("REDDIT_CLIENT_SECRET"))

# 🔑 Get Reddit API keys from .env
CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
USER_AGENT = "image_scraper:v1.0 (by u/yourusername)"  # safe to keep here

# Initialize Reddit instance
reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT
)

# Choose subreddit
subreddit = reddit.subreddit("iphone")

# 10 pages * 25 posts ≈ 250 posts
posts = subreddit.hot(limit=250)

data = []
for post in posts:
    # Only keep posts with images
    if post.url.endswith((".jpg", ".jpeg", ".png")):
        data.append({
            "title": post.title,
            "url": post.url,
            "subreddit": post.subreddit.display_name,
            "author": str(post.author),
            "upvotes": post.score,
            "created_utc": post.created_utc
        })

# Save to JSON file
with open("iphone_images.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f"✅ Saved {len(data)} image posts to iphone_images.json")




