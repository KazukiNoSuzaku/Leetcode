# Find the k-th smallest absolute difference among all pairs in an array.

# Author: Kaustav Ghosh

class Solution(object):
    def smallestDistancePair(self, nums, k):
        nums.sort()
        n = len(nums)
        lo, hi = 0, nums[-1] - nums[0]
        while lo < hi:
            mid = (lo + hi) // 2
            count = left = 0
            for right in range(n):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            if count >= k: hi = mid
            else: lo = mid + 1
        return lo
