'''LRU (Least Recently Used) Cache Using a Dictionary
Problem

Design an LRU Cache with the following operations:

get(key) → Return the value if present; otherwise return -1.
put(key, value) → Insert/update the key. If the cache exceeds its capacity, remove the least recently used item.
'''

from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):

        if key in self.cache:
            self.cache.move_to_end(key)

        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

cache = LRUCache(2)

cache.put(1, 10)
cache.put(2, 20)

print(cache.get(1))

cache.put(3, 30)

print(cache.get(2))

cache.put(4, 40)

print(cache.get(1))
print(cache.get(3))
print(cache.get(4))