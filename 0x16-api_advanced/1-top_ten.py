#!/usr/bin/python3
"""This module supplies the `top_ten` function
"""
import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"user-agent": "destino"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        posts = response.json()["data"]["children"]
        for post in posts:
            print(post["data"]["title"])
    else:
        print(None)
