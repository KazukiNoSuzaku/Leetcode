# Author: Kaustav Ghosh
# 2317. Maximum XOR After Operations
# XOR all elements: each bit is independently achievable via AND operations

class Solution(object):
    def maximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Key insight: we can perform nums[i] &= x for any x on any element.
        # This means we can zero out any bit of any element independently.
        # So any bit that appears in ANY element can be set in the XOR result.
        # The maximum XOR is simply the OR of all elements.
        result = 0
        for num in nums:
            result |= num
        return result
