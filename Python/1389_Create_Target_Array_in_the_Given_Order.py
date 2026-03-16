# Author: Kaustav Ghosh
# Problem: Create Target Array in the Given Order
# Approach: Simulate insertions at given indices

class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        target = []
        for n, i in zip(nums, index):
            target.insert(i, n)
        return target
