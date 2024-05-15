def count_calls(method: Callable) -> Callable:
    """
    count calls function decorate
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper for decorator functionality
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper
