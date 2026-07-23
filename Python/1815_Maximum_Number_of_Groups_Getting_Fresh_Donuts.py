# Author: Kaustav Ghosh
# Problem: Maximum Number of Groups Getting Fresh Donuts
# Approach: Only remainders mod batchSize matter. Groups with remainder 0 are always happy; for the rest, memoized DFS over the remaining remainder-count vector places groups, earning a point whenever the current leftover is 0

from functools import lru_cache
from collections import Counter

class Solution(object):
    def maxHappyGroups(self, batchSize, groups):
        """
        :type batchSize: int
        :type groups: List[int]
        :rtype: int
        """
        remainders = Counter(g % batchSize for g in groups)
        base = remainders[0]  # a remainder-0 group is always fresh
        counts = [remainders[r] for r in range(batchSize)]
        counts[0] = 0

        @lru_cache(maxsize=None)
        def dfs(state, leftover):
            best = 0
            cnts = list(state)
            for r in range(1, batchSize):
                if cnts[r] > 0:
                    cnts[r] -= 1
                    gain = 1 if leftover == 0 else 0
                    best = max(best, gain + dfs(tuple(cnts), (leftover + r) % batchSize))
                    cnts[r] += 1
            return best

        return base + dfs(tuple(counts), 0)
