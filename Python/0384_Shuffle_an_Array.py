# Given an integer array nums, design an algorithm to randomly shuffle the array.
# All permutations of the array should be equally likely as a result of the shuffling.
# Implement the Solution class with reset() and shuffle().

# Example 1:
# Input: ["Solution","shuffle","reset","shuffle"]
#        [[[1,2,3]],[],[],[]]
# Output: [null,[3,1,2],[1,2,3],[1,3,2]]

# Constraints:
# 1 <= nums.length <= 200
# -10^6 <= nums[i] <= 10^6
# All the elements of nums are unique.
# At most 5 * 10^4 calls in total will be made to reset and shuffle.

# Author: Kaustav Ghosh

import random

class Solution(object):
    def __init__(self, nums):
        self.original = nums[:]
        self.nums = nums

    def reset(self):
        self.nums[:] = self.original
        return self.nums

    def shuffle(self):
        n = len(self.nums)
        for i in range(n):
            j = random.randint(i, n - 1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums
