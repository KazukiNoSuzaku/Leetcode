# Author: Kaustav Ghosh
# Problem: Most Frequent Even Element
# Approach: Count only the even values; the answer is the smallest value among those tied for the highest count, or -1 when no even value appears at all

from collections import Counter


class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(x for x in nums if x % 2 == 0)
        if not count:
            return -1
        best = max(count.values())
        return min(x for x, c in count.items() if c == best)
