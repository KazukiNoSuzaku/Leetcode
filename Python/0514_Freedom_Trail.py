# In the video game Fallout 4, the mission "Road to Freedom" requires players to reach a key word
# on a ring. Given string ring and key word, return minimum steps to spell key.

# Author: Kaustav Ghosh

from collections import defaultdict

class Solution(object):
    def findRotateSteps(self, ring, key):
        n = len(ring)
        pos = defaultdict(list)
        for i, c in enumerate(ring):
            pos[c].append(i)
        from functools import lru_cache
        @lru_cache(maxsize=None)
        def dp(ki, ri):
            if ki == len(key): return 0
            best = float('inf')
            for ni in pos[key[ki]]:
                diff = abs(ri - ni)
                best = min(best, min(diff, n - diff) + 1 + dp(ki + 1, ni))
            return best
        return dp(0, 0)
