# Author: Kaustav Ghosh
# Problem: Minimum Operations to Make a Subsequence
# Approach: Insertions needed = len(target) - LCS(target, arr). target has distinct values, so map arr onto target indices and the LCS becomes a longest strictly increasing subsequence (patience/bisect)

from bisect import bisect_left

class Solution(object):
    def minOperations(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: int
        """
        index_of = {v: i for i, v in enumerate(target)}
        seq = [index_of[x] for x in arr if x in index_of]

        tails = []
        for x in seq:
            i = bisect_left(tails, x)
            if i == len(tails):
                tails.append(x)
            else:
                tails[i] = x

        return len(target) - len(tails)
