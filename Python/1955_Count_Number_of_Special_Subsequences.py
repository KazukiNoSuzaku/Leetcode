# Author: Kaustav Ghosh
# https://leetcode.com/problems/count-number-of-special-subsequences/

class Solution(object):
    def countSpecialSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        # dp[0] = ways to form subsequence of 0s
        # dp[1] = ways to form subsequence of 0s followed by 1s
        # dp[2] = ways to form subsequence of 0s, 1s, then 2s
        dp = [0, 0, 0]
        for num in nums:
            if num == 0:
                dp[0] = (2 * dp[0] + 1) % MOD
            elif num == 1:
                dp[1] = (2 * dp[1] + dp[0]) % MOD
            else:
                dp[2] = (2 * dp[2] + dp[1]) % MOD
        return dp[2]
