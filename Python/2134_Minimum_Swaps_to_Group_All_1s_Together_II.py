# Author: Kaustav Ghosh
# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/

class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_ones = sum(nums)
        if total_ones == 0:
            return 0
        n = len(nums)
        # Count ones in first window
        current_ones = sum(nums[:total_ones])
        max_ones = current_ones
        for i in range(1, n):
            current_ones += nums[(i + total_ones - 1) % n] - nums[i - 1]
            max_ones = max(max_ones, current_ones)
        return total_ones - max_ones
