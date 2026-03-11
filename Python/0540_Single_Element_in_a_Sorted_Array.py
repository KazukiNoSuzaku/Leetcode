# You are given a sorted array consisting of only integers where every element appears exactly
# twice, except for one element which appears exactly once. Find this single element.

# Author: Kaustav Ghosh

class Solution(object):
    def singleNonDuplicate(self, nums):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if mid % 2 == 1: mid -= 1
            if nums[mid] == nums[mid + 1]:
                lo = mid + 2
            else:
                hi = mid
        return nums[lo]
