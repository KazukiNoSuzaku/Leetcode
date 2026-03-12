# Author: Kaustav Ghosh
# DP hashmap: dp[val] = length of longest arithmetic subsequence ending with val

class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        dp = {}
        result = 1
        for num in arr:
            dp[num] = dp.get(num - difference, 0) + 1
            result = max(result, dp[num])
        return result
