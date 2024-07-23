#!/usr/bin/env python3
""" BasicCache module """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.order.remove(key)

        elif len(self.order) >= BaseCaching.MAX_ITEMS:
            removed = self.order.pop(-1)
            del self.cache_data[removed]
            print("DISCARD: {}".format(removed))

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data.get(key)
        return None
