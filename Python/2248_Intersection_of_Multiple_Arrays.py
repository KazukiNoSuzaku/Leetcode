# Author: Kaustav Ghosh
# Problem: Intersection of Multiple Arrays
# Approach: Intersect all the arrays as sets to find the values present in every array, then return them sorted

class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        common = set(nums[0])
        for arr in nums[1:]:
            common &= set(arr)
        return sorted(common)
