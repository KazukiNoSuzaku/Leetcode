# Author: Kaustav Ghosh
# Problem: Maximum Sum Score of Array
# Approach: For each index the score is the larger of the prefix sum ending there and the suffix sum starting there. Track the running prefix sum; the suffix sum is total minus the prefix before that index. Take the maximum score over all indices

class Solution(object):
    def maximumSumScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        prefix = 0
        best = float('-inf')
        for x in nums:
            prefix += x
            suffix = total - (prefix - x)
            best = max(best, prefix, suffix)
        return best
