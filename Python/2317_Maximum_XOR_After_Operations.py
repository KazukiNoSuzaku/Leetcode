# Author: Kaustav Ghosh
# Problem: Maximum XOR After Operations
# Approach: The operation nums[i] = nums[i] AND (nums[i] XOR x) can clear any subset of a number's set bits (the result is always a submask of the original). So any bit that appears in some element can be kept in exactly one element and cleared elsewhere, making the maximum XOR equal to the bitwise OR of all elements

class Solution(object):
    def maximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for x in nums:
            result |= x
        return result
