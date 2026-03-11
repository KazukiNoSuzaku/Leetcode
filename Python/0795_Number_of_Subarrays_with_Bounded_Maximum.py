# Count subarrays where the max element is in [left, right].

# Author: Kaustav Ghosh

class Solution(object):
    def numSubarrayBoundedMax(self, nums, left, right):
        def count(bound):
            res = cur = 0
            for n in nums:
                cur = cur + 1 if n <= bound else 0
                res += cur
            return res
        return count(right) - count(left - 1)
