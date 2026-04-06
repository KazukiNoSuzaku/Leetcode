# Author: Kaustav Ghosh
# Problem: 2219. Maximum Sum Score of Array
# URL: https://leetcode.com/problems/maximum-sum-score-of-array/
# Difficulty: Medium (Premium)
#
# Approach:
# The score at index i is max(prefix_sum[i], suffix_sum[i]).
# prefix_sum[i] = sum(nums[0..i]), suffix_sum[i] = sum(nums[i..n-1]).
# Compute the total sum first, then walk left to right maintaining a running
# prefix sum. suffix_sum[i] = total - prefix_sum[i-1].

class Solution(object):
    def maximumSumScore(self, nums):
        """
        :type nums: list[int]
        :rtype: int
        """
        total = sum(nums)
        prefix = 0
        best = float('-inf')
        for num in nums:
            prefix += num
            suffix = total - prefix + num
            best = max(best, prefix, suffix)
        return best
