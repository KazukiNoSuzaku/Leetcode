# Author: Kaustav Ghosh
# Problem 2089: Find Target Indices After Sorting Array

class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        less = 0
        equal = 0
        for num in nums:
            if num < target:
                less += 1
            elif num == target:
                equal += 1
        return list(range(less, less + equal))
