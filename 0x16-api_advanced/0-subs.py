#!/usr/bin/python3
"""This module supplies the `number_of_subscribers` function
"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers for
    a given subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"user-agent": "destino"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return (data["data"]["subscribers"])
    else:
        return (0)
