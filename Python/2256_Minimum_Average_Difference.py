# Author: Kaustav Ghosh
# Problem: Minimum Average Difference
# Approach: Track the running prefix sum and the total; at each index the average difference is the absolute gap between the floored average of the first i+1 elements and the floored average of the rest (0 when the rest is empty). Return the earliest index achieving the minimum

class Solution(object):
    def minimumAverageDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = sum(nums)
        prefix = 0
        best_idx = 0
        best_val = None
        for i in range(n):
            prefix += nums[i]
            left_avg = prefix // (i + 1)
            right_count = n - i - 1
            right_avg = (total - prefix) // right_count if right_count > 0 else 0
            diff = abs(left_avg - right_avg)
            if best_val is None or diff < best_val:
                best_val = diff
                best_idx = i
        return best_idx
