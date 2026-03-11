# An array is squareful if the sum of every pair of adjacent elements is a perfect square.
# Return the number of permutations of nums that are squareful.

# Author: Kaustav Ghosh

import math
from collections import Counter

class Solution(object):
    def numSquarefulPerms(self, nums):
        count = Counter(nums)
        def is_square(n):
            r = int(math.sqrt(n))
            return r * r == n
        graph = {x: [] for x in count}
        for x in count:
            for y in count:
                if is_square(x + y):
                    graph[x].append(y)
        self.res = 0
        def dfs(prev, remaining):
            if remaining == 0:
                self.res += 1
                return
            for nxt in graph[prev]:
                if count[nxt] > 0:
                    count[nxt] -= 1
                    dfs(nxt, remaining - 1)
                    count[nxt] += 1
        total = len(nums)
        for x in list(count):
            count[x] -= 1
            dfs(x, total - 1)
            count[x] += 1
        return self.res
