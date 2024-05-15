#!/usr/bin/env python3
"""
Practice with redis
"""
import uuid
import redis
from typing import Union
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    count calls function decorate
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper for decorator functionality
        """
        self._redis.incr(key)

        return method(self, *args, **kwargs)
    return wrapper


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

    #!/usr/bin/env python3
"""
Practice with redis
"""
import uuid
import redis
from typing import Callable, Union


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

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float, None]:
        """
        Get data from redis
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """
        get str method
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """
        get int method
        """
        return self.get(key, fn=int)
