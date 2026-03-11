# Design a time-based key-value data structure that supports set and get operations
# where get returns the value with the largest timestamp <= given timestamp.

# Author: Kaustav Ghosh

import bisect

class TimeMap(object):
    def __init__(self):
        self.store = {}

    def set(self, key, value, timestamp):
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key, timestamp):
        if key not in self.store:
            return ''
        arr = self.store[key]
        i = bisect.bisect_right(arr, (timestamp, chr(127)))
        return arr[i-1][1] if i > 0 else ''
