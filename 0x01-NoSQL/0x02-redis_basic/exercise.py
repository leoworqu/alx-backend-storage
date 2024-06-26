#!/usr/bin/env python3
"""
Practice with redis
"""
import uuid
import redis
from typing import Union


class Cache:
    """
    Redis Cache Class
    """
    def __init__(self):
        """
        Constructor
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in redis
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
