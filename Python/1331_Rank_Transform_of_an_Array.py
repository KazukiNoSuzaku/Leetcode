# Replace each element with its rank (1-indexed, smallest = rank 1).
# Equal elements get the same rank.

# Author: Kaustav Ghosh

class Solution(object):
    def arrayRankTransform(self, arr):
        rank = {v: i+1 for i, v in enumerate(sorted(set(arr)))}
        return [rank[x] for x in arr]
