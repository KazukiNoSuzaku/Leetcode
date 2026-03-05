# Given an integer array of size n, find all elements that appear more than n/3 times.

# Example 1:
# Input: nums = [3,2,3]
# Output: [3]

# Example 2:
# Input: nums = [1]
# Output: [1]

# Example 3:
# Input: nums = [1,2]
# Output: [1,2]

# Constraints:
# 1 <= nums.length <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9

# Author: Kaustav Ghosh

class Solution(object):
    def majorityElement(self, nums):
        cand1 = cand2 = None
        count1 = count2 = 0
        for n in nums:
            if n == cand1:
                count1 += 1
            elif n == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = n, 1
            elif count2 == 0:
                cand2, count2 = n, 1
            else:
                count1 -= 1
                count2 -= 1
        threshold = len(nums) // 3
        return [c for c in (cand1, cand2) if c is not None and nums.count(c) > threshold]
