# Author: Kaustav Ghosh
# Problem: Maximum Length of Subarray With Positive Product
# Approach: Track the length of the longest subarray ending here with positive and with negative product; reset both at any zero

class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = neg = 0
        best = 0
        for x in nums:
            if x == 0:
                pos = neg = 0
            elif x > 0:
                pos += 1
                neg = neg + 1 if neg > 0 else 0
            else:  # negative flips the signs
                new_pos = neg + 1 if neg > 0 else 0
                new_neg = pos + 1
                pos, neg = new_pos, new_neg
            best = max(best, pos)
        return best
