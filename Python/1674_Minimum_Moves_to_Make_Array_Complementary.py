# Author: Kaustav Ghosh
# Problem: Minimum Moves to Make Array Complementary
# Approach: Each pair costs 2 by default, 1 for target sums reachable by changing one element, 0 at its current sum; a difference array over all target sums gives the cheapest common target

class Solution(object):
    def minMoves(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        n = len(nums)
        delta = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            lo = min(a, b) + 1          # from here one change suffices
            hi = max(a, b) + limit      # last sum reachable with one change
            s = a + b                   # zero changes needed exactly here

            delta[2] += 2
            delta[lo] -= 1
            delta[s] -= 1
            delta[s + 1] += 1
            delta[hi + 1] += 1

        best = float('inf')
        cur = 0
        for target in range(2, 2 * limit + 1):
            cur += delta[target]
            best = min(best, cur)
        return best
