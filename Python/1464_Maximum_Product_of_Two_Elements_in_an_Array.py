# Author: Kaustav Ghosh
# Problem: Maximum Product of Two Elements in an Array
# Approach: Find two largest elements and multiply (each minus 1)

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)
