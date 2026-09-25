# Author: Kaustav Ghosh
# Problem: Apply Operations to an Array
# Approach: The operations are applied in order from the left, each only touching a neighbouring pair, so one left-to-right pass performs them all. Afterwards keep the non-zero values in order and pad the rest of the length with zeros

class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        values = nums[:]
        for i in range(len(values) - 1):
            if values[i] == values[i + 1]:
                values[i] *= 2
                values[i + 1] = 0
        result = [x for x in values if x]
        return result + [0] * (len(values) - len(result))
