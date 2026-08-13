# Author: Kaustav Ghosh
# Problem: Count Number of Pairs With Absolute Difference K
# Approach: For each value, the pairs it forms with earlier values differing by k are the counts of value-k and value+k already seen. Accumulate while building the frequency map

from collections import Counter

class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        seen = Counter()
        pairs = 0
        for v in nums:
            pairs += seen[v - k] + seen[v + k]
            seen[v] += 1
        return pairs
