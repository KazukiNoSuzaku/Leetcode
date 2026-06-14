from typing import List
import bisect

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)

        # Longest strictly increasing prefix: nums[0..left]
        left = 0
        while left + 1 < n and nums[left] < nums[left + 1]:
            left += 1

        if left == n - 1:
            return n * (n + 1) // 2

        # Smallest index right where nums[right..n-1] is strictly increasing
        right = n - 1
        while right - 1 >= 0 and nums[right - 1] < nums[right]:
            right -= 1

        # Remove subarray nums[i..j]; remaining = nums[0..i-1] + nums[j+1..n-1]
        # Count valid (i, j) pairs (0-indexed, i <= j).
        # For suffix starting at s = j+1 (s=n means empty suffix):
        #   s >= right for suffix to be strictly increasing
        #   i can be 0..min(left+1, s-1) for prefix to be strictly increasing
        #   if i > 0 and s < n: need nums[i-1] < nums[s]

        # Case: empty suffix (s = n, j = n-1)
        ans = left + 2  # i in [0, left+1]

        # Case: suffix starts at s in [right, n-1]
        for s in range(right, n):
            if s == 0:
                continue  # j = -1 is invalid
            # Search limit: i-1 in [0, min(left, s-2)], i.e. hi = min(left+1, s-1)
            hi = min(left + 1, s - 1)
            # Number of valid i in [1, hi] with nums[i-1] < nums[s]
            valid_with_prefix = bisect.bisect_left(nums, nums[s], 0, hi)
            ans += valid_with_prefix + 1  # +1 for i=0 (empty prefix)

        return ans
