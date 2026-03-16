# Author: Kaustav Ghosh
# Problem: Least Number of Unique Integers after K Removals
# Approach: Sort by frequency, remove rarest integers first

from collections import Counter

class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        freq = sorted(Counter(arr).values())
        removed = 0
        for f in freq:
            if k >= f:
                k -= f
                removed += 1
            else:
                break
        return len(freq) - removed
