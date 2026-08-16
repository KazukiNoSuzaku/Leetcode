# Author: Kaustav Ghosh
# Problem: Minimum Operations to Make a Uni-Value Grid
# Approach: Every element changes by multiples of x, so a common value exists only if all elements share the same remainder mod x. Then the median target minimizes the total number of x-steps, which is the sum of absolute differences divided by x

class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        vals = sorted(v for row in grid for v in row)
        r = vals[0] % x
        if any(v % x != r for v in vals):
            return -1
        median = vals[len(vals) // 2]
        return sum(abs(v - median) // x for v in vals)
