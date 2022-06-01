#!/usr/bin/python3
"""This module supplies the `recurse` function
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"user-agent": "destino"}
    params = {"after": after, "limit": 100}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        json = response.json()
        after = json["data"]["after"]
        posts = json["data"]["children"]
        for post in posts:
            hot_list.append(post["data"]["title"])
        if after is None:
            return (hot_list)
        return (recurse(subreddit, hot_list, after))
    else:
        return None
