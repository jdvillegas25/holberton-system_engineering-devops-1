#!/usr/bin/python3
"""
Module for a function that returns the number of subscribers in a subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
        Returns the number of subscribers to a specified subreddit
    """
    url = 'https://www.reddit.com/r/{}/about/.json'.format(subreddit)
    req = requests.get(url).json()
    data = req.get('data')
    return data.get('subscribers')
