# Author: Kaustav Ghosh
# Problem: Minimum Subsequence in Non-Increasing Order
# Approach: Sort desc, take elements until their sum exceeds the rest

class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort(reverse=True)
        total = sum(nums)
        result = []
        current = 0
        for n in nums:
            current += n
            result.append(n)
            if current > total - current:
                break
        return result
