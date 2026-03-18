# Author: Kaustav Ghosh
# Problem: 1567 - Maximum Length of Subarray With Positive Product
# Approach: Track lengths of current subarray with positive and negative product

class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = 0  # length of subarray ending here with positive product
        neg = 0  # length of subarray ending here with negative product
        result = 0

        for num in nums:
            if num == 0:
                pos = neg = 0
            elif num > 0:
                pos = pos + 1
                neg = neg + 1 if neg > 0 else 0
            else:
                pos, neg = neg + 1 if neg > 0 else 0, pos + 1
            result = max(result, pos)

        return result
