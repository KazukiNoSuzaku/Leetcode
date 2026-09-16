# Author: Kaustav Ghosh
# Problem: Merge Similar Items
# Approach: Add the weights of both lists into a map keyed by value, then return the entries sorted by value

from collections import defaultdict


class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """
        totals = defaultdict(int)
        for value, weight in items1 + items2:
            totals[value] += weight
        return [[value, totals[value]] for value in sorted(totals)]
