# Author: Kaustav Ghosh
# https://leetcode.com/problems/ways-to-make-a-fair-array/

class Solution(object):
    def waysToMakeFair(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        right_even = sum(nums[i] for i in range(0, n, 2))
        right_odd = sum(nums[i] for i in range(1, n, 2))
        left_even = 0
        left_odd = 0
        count = 0
        for i in range(n):
            if i % 2 == 0:
                right_even -= nums[i]
            else:
                right_odd -= nums[i]
            # After removing i: left stays, right even/odd swap
            if left_even + right_odd == left_odd + right_even:
                count += 1
            if i % 2 == 0:
                left_even += nums[i]
            else:
                left_odd += nums[i]
        return count
