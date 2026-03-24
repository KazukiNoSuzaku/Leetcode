# Author: Kaustav Ghosh
# Problem 2053: Kth Distinct String in an Array

from collections import Counter

class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        freq = Counter(arr)
        count = 0
        for s in arr:
            if freq[s] == 1:
                count += 1
                if count == k:
                    return s
        return ""
