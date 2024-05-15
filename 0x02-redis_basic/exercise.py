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


def call_history(method: Callable) -> Callable:
    """
    Wrapper for decorator functionality
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper for decorator functionality
        """
        inputs_key = method.__qualname__ + ":inputs"
        outputs_key = method.__qualname__ + ":outputs"
        
        self._redis.rpush(inputs_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, str(output))
        
        return output
    return wrapper


def replay(fn: Callable):
    """
    Display the history of calls of a particular function
    """
    r = redis.Redis()
    f_name = fn.__qualname__
    n_calls = r.get(f_name)
    try:
        n_calls = n_calls.decode('utf-8')
    except Exception:
        n_calls = 0
    print(f'{f_name} was called {n_calls} times:')
    inside = r.lrange(f_name + ":inputs", 0, -1)
    outside = r.lrange(f_name + ":outputs", 0, -1)
    for key, value in zip(inside, outside):
        try:
            key = key.decode('utf-8')
        except Exception:
            key = ""
        try:
            value = value.decode('utf-8')
        except Exception:
            value = ""
        print(f'{f_name}(*{key}) -> {value}')


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
