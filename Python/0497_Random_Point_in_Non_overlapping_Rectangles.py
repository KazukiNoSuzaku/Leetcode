# You are given an array of non-overlapping axis-aligned rectangles rects where
# rects[i] = [ai, bi, xi, yi] indicates that (ai, bi) is the bottom-left corner and
# (xi, yi) is the top-right corner of the ith rectangle. Return a random integer point [u, v]
# inside the space covered by one of the given rectangles.

# Author: Kaustav Ghosh

import random
import bisect

class Solution(object):
    def __init__(self, rects):
        self.rects = rects
        self.weights = []
        total = 0
        for a, b, x, y in rects:
            total += (x - a + 1) * (y - b + 1)
            self.weights.append(total)
        self.total = total

    def pick(self):
        r = random.randint(1, self.total)
        idx = bisect.bisect_left(self.weights, r)
        a, b, x, y = self.rects[idx]
        return [random.randint(a, x), random.randint(b, y)]
