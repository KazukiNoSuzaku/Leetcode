# Two fingers on a phone keyboard. Return min total distance to type the word.
# Distance between keys = |r1-r2| + |c1-c2| on a 6x4 grid.

# Author: Kaustav Ghosh

class Solution(object):
    def minimumDistance(self, word):
        def dist(a, b):
            if a is None: return 0
            return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)
        # dp[(f1, f2)] = min cost, one finger just typed current char
        # Start: both fingers unplaced
        dp = {(None, None): 0}
        for c in word:
            pos = ord(c) - ord('A')
            ndp = {}
            for (f1, f2), cost in dp.items():
                # Move f1 to pos
                key = (pos, f2)
                ndp[key] = min(ndp.get(key, float('inf')), cost + dist(f1, pos))
                # Move f2 to pos
                key = (f1, pos)
                ndp[key] = min(ndp.get(key, float('inf')), cost + dist(f2, pos))
            dp = ndp
        return min(dp.values())
