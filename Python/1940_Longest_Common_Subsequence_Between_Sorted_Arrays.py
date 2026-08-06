# Author: Kaustav Ghosh
# Problem: Longest Common Subsequence Between Sorted Arrays
# Approach: Each array is strictly increasing (distinct values), so the common subsequence is exactly the set of values present in every array. Count occurrences across arrays and keep those seen in all of them, in sorted order

from collections import Counter

class Solution(object):
    def longestCommonSubsequence(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: List[int]
        """
        k = len(arrays)
        counts = Counter()
        for arr in arrays:
            counts.update(arr)
        return [v for v in sorted(counts) if counts[v] == k]
