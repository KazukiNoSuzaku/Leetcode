# Given an integer array nums and an integer k, split nums into k non-empty subarrays
# such that the largest sum of any subarray is minimized. Return the minimized largest sum.

# Author: Kaustav Ghosh

class Solution(object):
    def splitArray(self, nums, k):
        def can_split(mid):
            count, cur = 1, 0
            for n in nums:
                if cur + n > mid:
                    count += 1
                    cur = 0
                cur += n
            return count <= k

        lo, hi = max(nums), sum(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if can_split(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
