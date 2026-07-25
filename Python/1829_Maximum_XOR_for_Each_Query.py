# Author: Kaustav Ghosh
# Problem: Maximum XOR for Each Query
# Approach: The best k always turns the running XOR into all ones within maximumBit, so k = xor ^ mask. Process queries by removing elements from the end, XOR-ing each out

class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        """
        :type nums: List[int]
        :type maximumBit: int
        :rtype: List[int]
        """
        mask = (1 << maximumBit) - 1
        xor = 0
        for x in nums:
            xor ^= x

        res = []
        for x in reversed(nums):
            res.append(xor ^ mask)
            xor ^= x  # remove the last element for the next query
        return res
