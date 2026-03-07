# Given an integer array nums, handle multiple queries of the following types:
# 1. Update the value of an element in nums.
# 2. Calculate the sum of the elements of nums between indices left and right inclusive.
# Implement the NumArray class:
# - NumArray(int[] nums) Initializes the object with the integer array nums.
# - void update(int index, int val) Updates the value of nums[index] to be val.
# - int sumRange(int left, int right) Returns the sum of nums[left..right].

# Example 1:
# Input: ["NumArray","sumRange","update","sumRange"]
#        [[[1,3,5]],[0,2],[1,2],[0,2]]
# Output: [null,9,null,8]

# Constraints:
# 1 <= nums.length <= 3 * 10^4
# At most 3 * 10^4 calls will be made to update and sumRange.

# Author: Kaustav Ghosh

class NumArray(object):
    def __init__(self, nums):
        n = len(nums)
        self.n = n
        self.tree = [0] * (n + 1)
        for i, v in enumerate(nums):
            self._update(i + 1, v)

    def _update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)

    def _query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

    def update(self, index, val):
        old = self._query(index + 1) - self._query(index)
        self._update(index + 1, val - old)

    def sumRange(self, left, right):
        return self._query(right + 1) - self._query(left)
