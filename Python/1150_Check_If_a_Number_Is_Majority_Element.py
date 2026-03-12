# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Binary search for first and last occurrence in sorted array

class Solution(object):
    def isMajorityElement(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        import bisect
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)
        return right - left > len(nums) // 2
