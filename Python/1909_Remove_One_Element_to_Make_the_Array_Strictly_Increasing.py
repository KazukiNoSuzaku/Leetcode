# Author: Kaustav Ghosh
# Problem: Remove One Element to Make the Array Strictly Increasing
# Approach: At most one element may go, so the array is scanned for the first position where it fails to increase; everything before that point is already strictly increasing and untouchable. The only removals that can repair that failure are the two elements involved in it, since dropping anything else leaves the offending pair adjacent, so both are tried and the array is tested once for each. That makes the whole check two linear passes at worst rather than one per candidate removal.

class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def increasing(skip):
            previous = None
            for index, value in enumerate(nums):
                if index == skip:
                    continue
                if previous is not None and value <= previous:
                    return False
                previous = value
            return True

        for index in range(1, len(nums)):
            if nums[index] <= nums[index - 1]:
                return increasing(index - 1) or increasing(index)
        return True
