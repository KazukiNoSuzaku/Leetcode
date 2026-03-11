# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Author: Kaustav Ghosh

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_count = count = 0
        for n in nums:
            if n == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
        return max_count
