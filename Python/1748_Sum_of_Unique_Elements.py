# Author: Kaustav Ghosh
# Problem: Sum of Unique Elements
# Approach: Tally the values and add up those appearing exactly once

from collections import Counter

class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(value for value, count in Counter(nums).items() if count == 1)
