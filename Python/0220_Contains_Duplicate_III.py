# You are given an integer array nums and two integers indexDiff and valueDiff.
# Find a pair of indices (i, j) such that:
# - i != j
# - abs(i - j) <= indexDiff
# - abs(nums[i] - nums[j]) <= valueDiff
# Return true if such pair exists or false otherwise.

# Example 1:
# Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
# Output: true

# Example 2:
# Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
# Output: false

# Constraints:
# 2 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 1 <= indexDiff <= nums.length
# 0 <= valueDiff <= 10^9

# Author: Kaustav Ghosh

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        buckets = {}
        w = valueDiff + 1

        def get_bucket(x):
            return x // w if x >= 0 else (x + 1) // w - 1

        for i, n in enumerate(nums):
            b = get_bucket(n)
            if b in buckets:
                return True
            if b - 1 in buckets and abs(n - buckets[b - 1]) < w:
                return True
            if b + 1 in buckets and abs(n - buckets[b + 1]) < w:
                return True
            buckets[b] = n
            if i >= indexDiff:
                del buckets[get_bucket(nums[i - indexDiff])]
        return False
