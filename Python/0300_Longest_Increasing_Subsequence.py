# Given an integer array nums, return the length of the longest strictly increasing subsequence.

# Example 1:
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

# Example 2:
# Input: nums = [0,1,0,3,2,3]
# Output: 4

# Constraints:
# 1 <= nums.length <= 2500
# -10^4 <= nums[i] <= 10^4

# Author: Kaustav Ghosh

import bisect

class Solution(object):
    def lengthOfLIS(self, nums):
        tails = []
        for n in nums:
            pos = bisect.bisect_left(tails, n)
            if pos == len(tails):
                tails.append(n)
            else:
                tails[pos] = n
        return len(tails)
