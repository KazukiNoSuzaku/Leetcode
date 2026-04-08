# Author: Kaustav Ghosh
# Problem: 2239. Find Closest Number to Zero
# URL: https://leetcode.com/problems/find-closest-number-to-zero/
# Difficulty: Easy
#
# Approach:
# Iterate through the array tracking the number with the smallest absolute
# value. If two numbers have the same absolute value, prefer the positive one.

class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        closest = nums[0]
        for n in nums:
            if abs(n) < abs(closest) or (abs(n) == abs(closest) and n > closest):
                closest = n
        return closest
