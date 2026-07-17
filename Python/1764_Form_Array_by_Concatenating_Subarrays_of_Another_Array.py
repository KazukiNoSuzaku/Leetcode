# Author: Kaustav Ghosh
# Problem: Form Array by Concatenating Subarrays of Another Array
# Approach: Greedily match each group in order as a contiguous block in nums, advancing the pointer past a match so blocks stay disjoint

class Solution(object):
    def canChoose(self, groups, nums):
        """
        :type groups: List[List[int]]
        :type nums: List[int]
        :rtype: bool
        """
        i = 0
        for g in groups:
            k = len(g)
            found = False
            while i + k <= len(nums):
                if nums[i:i + k] == g:
                    i += k
                    found = True
                    break
                i += 1
            if not found:
                return False
        return True
