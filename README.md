# Reddit Image Scraper

A Python script that scrapes image posts from a chosen subreddit using the Reddit API (via PRAW)  
and saves the results into a JSON file.

## Features
- Connects to Reddit API using `praw`
- Collects up to 250 image posts from a chosen subreddit
- Saves post info (title, url, subreddit, author, upvotes, timestamp) into JSON
- Easy to extend (e.g., download images to local folder)

## Requirements
- Python 3.10+
- `praw`
- `python-dotenv`

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/natshaalya/reddit_image_scraper.git
   cd reddit_image_scraper
