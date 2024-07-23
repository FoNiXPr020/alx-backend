#!/usr/bin/env python3
""" BasicCache module """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return
        return self.cache_data.get(key)
