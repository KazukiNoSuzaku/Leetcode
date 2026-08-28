# Author: Kaustav Ghosh
# Problem: Sort Even and Odd Indices Independently
# Approach: Sort the values at even indices in ascending order and those at odd indices in descending order, then place each group back into its positions

class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even = sorted(nums[0::2])
        odd = sorted(nums[1::2], reverse=True)
        result = nums[:]
        result[0::2] = even
        result[1::2] = odd
        return result
