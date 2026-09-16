# Author: Kaustav Ghosh
# Problem: Check if There is a Valid Partition For The Array
# Approach: dp[i] says whether the first i elements split into valid blocks. A block is two equal elements, three equal elements, or three consecutive increasing by one, so dp[i] holds when dp[i - 2] or dp[i - 3] holds and the matching tail forms one of those blocks

class Solution(object):
    def validPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(2, n + 1):
            if dp[i - 2] and nums[i - 1] == nums[i - 2]:
                dp[i] = True
            elif i >= 3 and dp[i - 3] and (
                    nums[i - 1] == nums[i - 2] == nums[i - 3]
                    or nums[i - 1] == nums[i - 2] + 1 == nums[i - 3] + 2):
                dp[i] = True
        return dp[n]
