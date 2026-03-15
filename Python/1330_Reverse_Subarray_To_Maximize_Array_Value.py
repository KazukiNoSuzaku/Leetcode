# Reverse exactly one subarray to maximize the sum of |nums[i] - nums[i+1]|.

# Author: Kaustav Ghosh

class Solution(object):
    def maxValueAfterReverse(self, nums):
        n = len(nums)
        base = sum(abs(nums[i] - nums[i+1]) for i in range(n-1))
        gain = 0
        # Case 1: reverse subarray including one end
        for i in range(1, n-1):
            gain = max(gain,
                       abs(nums[0] - nums[i+1]) - abs(nums[i] - nums[i+1]),
                       abs(nums[n-1] - nums[i-1]) - abs(nums[i-1] - nums[i]))
        # Case 2: reverse middle subarray
        # For adjacent pairs (a,b) and (c,d): gain = 2*(min(max(a,b),max(c,d)) - max(min(a,b),min(c,d)))
        for i in range(n-1):
            a, b = nums[i], nums[i+1]
            for j in range(i+2, n-1):
                c, d = nums[j], nums[j+1]
                gain = max(gain, 2 * (min(max(a,b), max(c,d)) - max(min(a,b), min(c,d))))
        return base + gain
