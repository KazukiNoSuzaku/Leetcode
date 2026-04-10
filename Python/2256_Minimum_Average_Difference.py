# Author: Kaustav Ghosh
# Problem: 2256. Minimum Average Difference
# URL: https://leetcode.com/problems/minimum-average-difference/
# Difficulty: Medium
#
# Approach:
# Compute prefix sum. For each index i, left average = prefix[i+1]/(i+1),
# right average = (total - prefix[i+1])/(n-i-1) if i < n-1, else 0.
# Track index with minimum absolute difference.

class Solution(object):
    def minimumAverageDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = sum(nums)
        prefix = 0
        min_diff = float('inf')
        result = 0
        for i in range(n):
            prefix += nums[i]
            left_avg = prefix // (i + 1)
            if i < n - 1:
                right_avg = (total - prefix) // (n - i - 1)
            else:
                right_avg = 0
            diff = abs(left_avg - right_avg)
            if diff < min_diff:
                min_diff = diff
                result = i
        return result
