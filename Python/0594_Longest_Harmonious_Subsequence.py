# A harmonious array is an array where the difference between its max and min value is exactly 1.
# Given an integer array nums, return the length of its longest harmonious subsequence.

# Author: Kaustav Ghosh

from collections import Counter

class Solution(object):
    def findLHS(self, nums):
        count = Counter(nums)
        return max((count[n] + count[n+1] for n in count if n+1 in count), default=0)
