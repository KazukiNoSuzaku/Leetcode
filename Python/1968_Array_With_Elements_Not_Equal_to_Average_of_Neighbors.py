# Author: Kaustav Ghosh
# Problem: Array With Elements Not Equal to Average of Neighbors
# Approach: Wiggle-sort style. Sort, split into a smaller and larger half, reverse each, then place the smaller half at even positions and larger half at odd positions. Reversing keeps equal medians apart so every interior element is a strict local min or max, which cannot equal the average of its neighbors

class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        n = len(nums)
        half = (n + 1) // 2
        small = nums[:half][::-1]
        large = nums[half:][::-1]
        res = [0] * n
        res[::2] = small
        res[1::2] = large
        return res
