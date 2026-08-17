# Author: Kaustav Ghosh
# Problem: Kth Distinct String in an Array
# Approach: Count occurrences, then scan in original order collecting strings that appear exactly once; return the kth such string, or empty if fewer than k exist

from collections import Counter

class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        counts = Counter(arr)
        for s in arr:
            if counts[s] == 1:
                k -= 1
                if k == 0:
                    return s
        return ""
