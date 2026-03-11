# Count rectangles with corners at 1s in a binary grid.

# Author: Kaustav Ghosh

from collections import defaultdict

class Solution(object):
    def countCornerRectangles(self, grid):
        count = defaultdict(int)
        res = 0
        for row in grid:
            ones = [c for c, v in enumerate(row) if v]
            for i in range(len(ones)):
                for j in range(i+1, len(ones)):
                    pair = (ones[i], ones[j])
                    res += count[pair]
                    count[pair] += 1
        return res
