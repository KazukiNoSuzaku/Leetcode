# Author: Kaustav Ghosh
# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        target = sum(nums) - x
        if target < 0:
            return -1
        if target == 0:
            return len(nums)
        max_len = -1
        curr_sum = 0
        left = 0
        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum > target:
                curr_sum -= nums[left]
                left += 1
            if curr_sum == target:
                max_len = max(max_len, right - left + 1)
        return len(nums) - max_len if max_len != -1 else -1
