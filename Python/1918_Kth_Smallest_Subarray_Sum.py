# Author: Kaustav Ghosh
# Problem: Kth Smallest Subarray Sum
# Approach: Binary search the answer value. Since numbers are positive, the count of subarrays with sum <= x is monotonic and computable with a sliding window. Find the smallest x whose count reaches k

class Solution(object):
    def kthSmallestSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def count_le(x):
            total = 0
            left = 0
            window = 0
            for right in range(len(nums)):
                window += nums[right]
                while window > x:
                    window -= nums[left]
                    left += 1
                total += right - left + 1
            return total

        lo, hi = min(nums), sum(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if count_le(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
