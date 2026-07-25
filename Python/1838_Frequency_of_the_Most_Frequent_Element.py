# Author: Kaustav Ghosh
# Problem: Frequency of the Most Frequent Element
# Approach: Sort, then slide a window; raising all elements to the window's max costs max*width - windowSum, so shrink the window whenever that exceeds k

class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        left = 0
        window_sum = 0
        best = 1
        for right, val in enumerate(nums):
            window_sum += val
            while val * (right - left + 1) - window_sum > k:
                window_sum -= nums[left]
                left += 1
            best = max(best, right - left + 1)
        return best
