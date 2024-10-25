#!/usr/bin/env python3
"""exercise"""
import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        """
        Initializes the Cache instance with a Redis client
        and flushes the Redis database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the input data in Redis with a randomly generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
            str: The generated key for the stored data.
        """

        key = str(uuid.uuid4())

        self._redis.set(key, data)
        return key
