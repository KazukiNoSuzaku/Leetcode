# There is an m x n binary grid matrix with all the values set to 0 initially.
# Design an algorithm to randomly pick an index (i, j) where matrix[i][j] == 0 and flips it to 1.

# Author: Kaustav Ghosh

import random

class Solution(object):
    def __init__(self, m, n):
        self.m, self.n = m, n
        self.total = m * n
        self.flipped = {}

    def flip(self):
        r = random.randint(0, self.total - 1)
        self.total -= 1
        idx = self.flipped.get(r, r)
        self.flipped[r] = self.flipped.get(self.total, self.total)
        return [idx // self.n, idx % self.n]

    def reset(self):
        self.total = self.m * self.n
        self.flipped = {}
