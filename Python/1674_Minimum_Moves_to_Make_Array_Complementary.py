# Author: Kaustav Ghosh
# https://leetcode.com/problems/minimum-moves-to-make-array-complementary/

class Solution(object):
    def minMoves(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        n = len(nums)
        # Difference array approach
        delta = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            lo = min(a, b) + 1
            hi = max(a, b) + limit
            s = a + b

            # Range [2, 2*limit]: need 2 moves baseline
            delta[2] += 2
            # Range [lo, hi]: need only 1 move
            delta[lo] -= 1
            delta[hi + 1] += 1
            # Exact sum s: need 0 moves
            delta[s] -= 1
            delta[s + 1] += 1

        result = float('inf')
        curr = 0
        for t in range(2, 2 * limit + 1):
            curr += delta[t]
            result = min(result, curr)
        return result
