# Author: Kaustav Ghosh
# Problem 2033: Minimum Operations to Make a Uni-Value Grid

class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        vals = []
        for row in grid:
            for v in row:
                vals.append(v)
        # All values must have the same remainder mod x
        rem = vals[0] % x
        for v in vals:
            if v % x != rem:
                return -1
        vals.sort()
        median = vals[len(vals) // 2]
        ops = 0
        for v in vals:
            ops += abs(v - median) // x
        return ops
