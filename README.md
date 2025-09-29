# Reddit Image Scraper

A Python script that scrapes image posts from a chosen subreddit using the Reddit API (via PRAW) and saves the results into a JSON file.

## Features
- Connects to Reddit API using PRAW
- Collects up to 250 image posts from a chosen subreddit
- Saves post info (title, url, subreddit, author, upvotes, timestamp) into JSON
- Optional: HTML page to display results
- Easy to extend (e.g., download images to local folder)

## Requirements
- Python 3.10+
- praw
- python-dotenv
- requests (if downloading images)

## Installation
Clone this repository:
```bash
git clone https://github.com/natshaalya/reddit_image_scraper.git
cd reddit_image_scraper
Install dependencies:

bash
Copy code
pip install praw python-dotenv requests
Create a .env file in the root folder with your Reddit API credentials:

ini
Copy code
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
Usage
1️⃣ Run the scraper
bash
Copy code
python assessment.py
Metadata saved to iphone_images.json

Images downloaded to downloads/ (ignored in GitHub)

2️⃣ View results in HTML
Make sure index.html and iphone_images.json are in the same folder.

Start a local server:

bash
Copy code
python -m http.server 8000
Open your browser at http://localhost:8000/index.html
The page will show the post title and image from the JSON file.

Notes
.gitignore ensures .env and downloads/ folder are not uploaded.

You can manually include a few sample images if you want to preview them on GitHub.

yaml
Copy code

---

If you want, I can now give you the **exact `git` commands to replace your old README on GitHub** with this new one. Do you want me to do that?






