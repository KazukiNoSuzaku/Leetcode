# Find leftmost pivot index where sum of left equals sum of right.

# Author: Kaustav Ghosh

class Solution(object):
    def pivotIndex(self, nums):
        total = sum(nums)
        left = 0
        for i, n in enumerate(nums):
            if left == total - left - n:
                return i
            left += n
        return -1
