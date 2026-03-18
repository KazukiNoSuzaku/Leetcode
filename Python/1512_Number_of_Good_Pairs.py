# Author: Kaustav Ghosh
# Problem: 1512 - Number of Good Pairs
# Approach: count(x)*(count(x)-1)/2 for each value

from collections import Counter

class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        return sum(v * (v - 1) // 2 for v in count.values())
