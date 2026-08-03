# Author: Kaustav Ghosh
# Problem: Remove One Element to Make the Array Strictly Increasing
# Approach: Scan for the first descent nums[i-1] >= nums[i]. At most one removal is allowed: remove the earlier element when nums[i-2] < nums[i], otherwise remove nums[i]. A second violation means it is impossible

class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        removed = False
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                if removed:
                    return False
                removed = True
                # remove nums[i] (keep nums[i-1] as previous) when we must,
                # i.e. when nums[i-2] would still block nums[i]
                if i >= 2 and nums[i - 2] >= nums[i]:
                    nums[i] = nums[i - 1]
        return True
