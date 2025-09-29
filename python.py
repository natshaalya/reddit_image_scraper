import requests

url = "https://www.reddit.com/r/malaysia/.json"
headers = {"User-Agent": "Mozilla/5.0"}  # needed or Reddit may block you
response = requests.get(url, headers=headers)

data = response.json()  # convert response into Python dict
data["data"]["children"]
post = data["data"]["children"][0]["data"]

posts = []
for child in data["data"]["children"]:
    post = child["data"]
    title = post["title"]
    image_url = post.get("url_overridden_by_dest", "")
    
    # keep only if it's an image
    if image_url.endswith((".jpg", ".png", ".jpeg")):
        posts.append({"post_title": title, "image_url": image_url})

import json

with open("reddit_images.json", "w", encoding="utf-8") as f:
    json.dump(posts, f, indent=4, ensure_ascii=False)

[
    {
        "post_title": "KL skyline this morning 🌅",
        "image_url": "https://i.redd.it/klskyline1234.jpg"
    },
    {
        "post_title": "Street art in Penang 🎨",
        "image_url": "https://i.imgur.com/penangstreetart.jpg"
    }
]

