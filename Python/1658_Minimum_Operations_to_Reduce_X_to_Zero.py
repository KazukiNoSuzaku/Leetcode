# Author: Kaustav Ghosh
# Problem: Minimum Operations to Reduce X to Zero
# Approach: Removing ends to sum x is the complement of keeping a middle subarray summing to total-x; find the longest such subarray with a sliding window

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
        n = len(nums)
        if target == 0:
            return n

        best = -1
        left = 0
        cur = 0
        for right in range(n):
            cur += nums[right]
            while cur > target and left <= right:
                cur -= nums[left]
                left += 1
            if cur == target:
                best = max(best, right - left + 1)

        return n - best if best != -1 else -1
