# Author: Kaustav Ghosh
# Problem: Count Subarrays With Score Less Than K
# Approach: The score (sum times length) grows monotonically as a subarray extends, so use a sliding window. For each right endpoint, shrink the left boundary until the window's score is below k; every subarray ending at right and starting within the window is valid, contributing (right - left + 1)

class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        window_sum = 0
        count = 0
        for right, x in enumerate(nums):
            window_sum += x
            while (right - left + 1) * window_sum >= k:
                window_sum -= nums[left]
                left += 1
            count += right - left + 1
        return count
