# Author: Kaustav Ghosh
# DP tracking max sum for each remainder mod 3

class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0, float('-inf'), float('-inf')]
        for num in nums:
            new_dp = list(dp)
            for i in range(3):
                r = (i + num) % 3
                new_dp[r] = max(new_dp[r], dp[i] + num)
            dp = new_dp
        return dp[0]
