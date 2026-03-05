# Given an integer array nums, return the maximum difference between two successive elements
# in its sorted form. If the array contains less than two elements, return 0.
# You must write an algorithm that runs in linear time and uses linear extra space.

# Example 1:
# Input: nums = [3,6,9,1]
# Output: 3

# Example 2:
# Input: nums = [10]
# Output: 0

# Constraints:
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^9

# Author: Kaustav Ghosh

class Solution(object):
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        mn, mx = min(nums), max(nums)
        if mn == mx:
            return 0
        n = len(nums)
        bucket_size = max(1, (mx - mn) // (n - 1))
        bucket_count = (mx - mn) // bucket_size + 1
        buckets = [[float('inf'), float('-inf')] for _ in range(bucket_count)]
        for num in nums:
            idx = (num - mn) // bucket_size
            buckets[idx][0] = min(buckets[idx][0], num)
            buckets[idx][1] = max(buckets[idx][1], num)
        max_gap = 0
        prev_max = mn
        for lo, hi in buckets:
            if lo == float('inf'):
                continue
            max_gap = max(max_gap, lo - prev_max)
            prev_max = hi
        return max_gap
