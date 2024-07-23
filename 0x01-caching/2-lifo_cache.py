#!/usr/bin/env python3
""" LIFOCache module """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class """

    def __init__(self) -> None:
        """ Constructor """
        super().__init__()
        self.queue = []

    def put(self, key, item) -> None:
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.queue.remove(key)
            self.queue.append(key)
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = self.queue.pop()
            del self.cache_data[last_key]
            print("DISCARD: {}".format(last_key))
        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        """ Get an item by key """
        if key:
            return self.cache_data.get(key)
        return None
