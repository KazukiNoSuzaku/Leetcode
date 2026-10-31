# Author: Kaustav Ghosh
# Problem: Form Array by Concatenating Subarrays of Another Array
# Approach: The groups have to appear in order and without overlapping, so matching each group at the earliest position that still lies after the previous match is always safe: delaying a match can only push the remaining groups further right and never unlocks a placement that the earliest match blocked. A single pointer walks nums, compares the slice starting there against the current group, and on a hit jumps past the whole group before looking for the next one.

class Solution(object):
    def canChoose(self, groups, nums):
        """
        :type groups: List[List[int]]
        :type nums: List[int]
        :rtype: bool
        """
        position = 0
        for group in groups:
            size = len(group)
            while position + size <= len(nums) and nums[position:position + size] != group:
                position += 1
            if position + size > len(nums):
                return False
            position += size
        return True
