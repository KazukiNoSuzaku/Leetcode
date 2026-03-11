# You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.
# Implement pickIndex(), which randomly picks an index in the range [0, w.length - 1] with probability
# proportional to w[i].

# Author: Kaustav Ghosh

import random
import bisect

class Solution(object):
    def __init__(self, w):
        self.prefix = []
        total = 0
        for x in w:
            total += x
            self.prefix.append(total)
        self.total = total

    def pickIndex(self):
        r = random.randint(1, self.total)
        return bisect.bisect_left(self.prefix, r)
