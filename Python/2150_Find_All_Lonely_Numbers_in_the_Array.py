# Author: Kaustav Ghosh
# Problem: Find All Lonely Numbers in the Array
# Approach: A number is lonely if it occurs exactly once and neither its predecessor nor successor appears anywhere in the array

from collections import Counter

class Solution(object):
    def findLonely(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = Counter(nums)
        return [x for x in nums if count[x] == 1 and count[x - 1] == 0 and count[x + 1] == 0]
