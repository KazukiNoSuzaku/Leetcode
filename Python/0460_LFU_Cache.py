# Design and implement a data structure for a Least Frequently Used (LFU) cache.
# get(key) and put(key, value) must run in O(1) average time.

# Author: Kaustav Ghosh

from collections import defaultdict, OrderedDict

class LFUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.key_val = {}
        self.key_freq = {}
        self.freq_keys = defaultdict(OrderedDict)
        self.min_freq = 0

    def _update(self, key):
        freq = self.key_freq[key]
        self.key_freq[key] = freq + 1
        del self.freq_keys[freq][key]
        if not self.freq_keys[freq] and freq == self.min_freq:
            self.min_freq += 1
        self.freq_keys[freq + 1][key] = None

    def get(self, key):
        if key not in self.key_val:
            return -1
        self._update(key)
        return self.key_val[key]

    def put(self, key, value):
        if self.capacity <= 0:
            return
        if key in self.key_val:
            self.key_val[key] = value
            self._update(key)
        else:
            if len(self.key_val) >= self.capacity:
                evict_key, _ = self.freq_keys[self.min_freq].popitem(last=False)
                del self.key_val[evict_key]
                del self.key_freq[evict_key]
            self.key_val[key] = value
            self.key_freq[key] = 1
            self.freq_keys[1][key] = None
            self.min_freq = 1
