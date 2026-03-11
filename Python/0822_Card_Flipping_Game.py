# Find the smallest good integer (on front, not on back of same card).

# Author: Kaustav Ghosh

class Solution(object):
    def flipgame(self, fronts, backs):
        same = set(f for f, b in zip(fronts, backs) if f == b)
        res = float('inf')
        for x in fronts + backs:
            if x not in same:
                res = min(res, x)
        return res if res < float('inf') else 0
