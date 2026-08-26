# Author: Kaustav Ghosh
# Problem: Rearrange Array Elements by Sign
# Approach: Split the array into positives and negatives keeping their original order, then interleave them starting with a positive

class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        positives = [x for x in nums if x > 0]
        negatives = [x for x in nums if x < 0]
        result = []
        for p, n in zip(positives, negatives):
            result.append(p)
            result.append(n)
        return result
