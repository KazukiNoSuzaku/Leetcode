# Classic binary search for target in a sorted array.

# Author: Kaustav Ghosh

class Solution(object):
    def search(self, nums, target):
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target: return mid
            elif nums[mid] < target: lo = mid + 1
            else: hi = mid - 1
        return -1
