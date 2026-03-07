# Given an integer array nums and an integer k, return the maximum length of a subarray
# that sums to k. If there is not one, return 0 instead.

# Example 1:
# Input: nums = [1,-1,5,-2,3], k = 3
# Output: 4
# Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.

# Example 2:
# Input: nums = [-2,-1,2,1], k = 1
# Output: 2
# Explanation: The subarray [-1, 2] sums to 1 and is the longest.

# Constraints:
# 1 <= nums.length <= 2 * 10^5
# -10^4 <= nums[i] <= 10^4
# -10^9 <= k <= 10^9

# Author: Kaustav Ghosh

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        prefix = {0: -1}
        s = 0
        res = 0
        for i, n in enumerate(nums):
            s += n
            if s - k in prefix:
                res = max(res, i - prefix[s - k])
            if s not in prefix:
                prefix[s] = i
        return res
