# Author: Kaustav Ghosh
# 1090. Largest Values From Labels
# https://leetcode.com/problems/largest-values-from-labels/

from collections import Counter

class Solution(object):
    def largestValsFromLabels(self, values, labels, numWanted, useLimit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type numWanted: int
        :type useLimit: int
        :rtype: int
        """
        pairs = sorted(zip(values, labels), reverse=True)
        label_count = Counter()
        total = 0
        chosen = 0
        for val, label in pairs:
            if chosen == numWanted:
                break
            if label_count[label] < useLimit:
                total += val
                label_count[label] += 1
                chosen += 1
        return total
