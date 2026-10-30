# Author: Kaustav Ghosh
# Problem: Check if Array Is Sorted and Rotated
# Approach: A sorted array that has been rotated reads as two ascending stretches, so going round the array exactly once there can be at most one place where a value drops below its predecessor. Treating the array as circular, so the last element is compared against the first as well, makes the unrotated case fall out naturally: it has no drop at all, or the single drop is the wrap itself.

class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        drops = 0
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                drops += 1
        return drops <= 1
