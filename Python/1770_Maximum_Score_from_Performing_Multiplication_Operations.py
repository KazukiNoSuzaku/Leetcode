# Author: Kaustav Ghosh
# Problem: Maximum Score from Performing Multiplication Operations
# Approach: State is (ops done, taken from front) since the right index is then fixed. Roll the DP backward over operations, choosing front or back at each step

class Solution(object):
    def maximumScore(self, nums, multipliers):
        """
        :type nums: List[int]
        :type multipliers: List[int]
        :rtype: int
        """
        n = len(nums)
        m = len(multipliers)

        dp = [0] * (m + 1)  # dp[left] for the next operation index
        for i in range(m - 1, -1, -1):
            nxt = [0] * (m + 1)
            mult = multipliers[i]
            for left in range(i + 1):
                right = n - 1 - (i - left)
                nxt[left] = max(mult * nums[left] + dp[left + 1],
                                mult * nums[right] + dp[left])
            dp = nxt
        return dp[0]
