#!/usr/bin/env python3
"""
web module
"""
import requests
import time
from functools import wraps


CACHE = {}


def cache_decorator(func):
    """
    count requests decorate
    """
    @wraps(func)
    def wrapper(url):
        """
        Wrapper for decorator functionality
        """
        if url in CACHE and time.time() - CACHE[url]["timestamp"] < 10:
            CACHE[url]["count"] += 1
            return CACHE[url]["content"]
        else:
            content = func(url)
            CACHE[url] = {
                "content": content,
                "timestamp": time.time(),
                "count": 1
            }
            return content
    return wrapper

@cache_decorator
def get_page(url: str) -> str:
    """
    get page method
    """
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    """
    get google.com
    """
    url = "http://google.com"
    print(get_page(url))
    print(get_page(url))
    time.sleep(10)
    print(get_page(url))
