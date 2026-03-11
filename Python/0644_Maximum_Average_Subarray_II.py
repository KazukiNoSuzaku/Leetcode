# Find the contiguous subarray of length >= k with the maximum average.

# Author: Kaustav Ghosh

class Solution(object):
    def findMaxAverage(self, nums, k):
        def check(mid):
            shifted = [x - mid for x in nums]
            window = sum(shifted[:k])
            if window >= 0: return True
            prefix_min = 0
            prev_sum = 0
            for i in range(k, len(nums)):
                window += shifted[i]
                prev_sum += shifted[i - k]
                prefix_min = min(prefix_min, prev_sum)
                if window - prefix_min >= 0: return True
            return False
        lo, hi = min(nums), max(nums)
        for _ in range(100):
            mid = (lo + hi) / 2.0
            if check(mid): lo = mid
            else: hi = mid
        return lo
