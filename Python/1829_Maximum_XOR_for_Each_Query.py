# Author: Kaustav Ghosh

class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        """
        :type nums: List[int]
        :type maximumBit: int
        :rtype: List[int]
        """
        mask = (1 << maximumBit) - 1
        xor_all = 0
        for n in nums:
            xor_all ^= n
        res = []
        for i in range(len(nums) - 1, -1, -1):
            res.append(xor_all ^ mask)
            xor_all ^= nums[i]
        return res
