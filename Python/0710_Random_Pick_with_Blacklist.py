# Pick a random integer from [0, n) excluding blacklisted numbers uniformly.

# Author: Kaustav Ghosh

import random

class Solution(object):
    def __init__(self, n, blacklist):
        self.m = n - len(blacklist)
        bl_set = set(blacklist)
        self.remap = {}
        j = self.m
        for b in blacklist:
            if b < self.m:
                while j in bl_set: j += 1
                self.remap[b] = j
                j += 1

    def pick(self):
        r = random.randrange(self.m)
        return self.remap.get(r, r)
