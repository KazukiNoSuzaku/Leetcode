# Author: Kaustav Ghosh
# https://leetcode.com/problems/maximum-alternating-subsequence-sum/

class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even = 0  # max sum when next element to pick is at even index
        odd = 0   # max sum when next element to pick is at odd index
        for num in nums:
            new_even = max(even, odd + num)
            new_odd = max(odd, even - num)
            even = new_even
            odd = new_odd
        return even
