# Author: Kaustav Ghosh
# 1128. Number of Equivalent Domino Pairs
# https://leetcode.com/problems/number-of-equivalent-domino-pairs/

from collections import Counter

class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        count = Counter()
        result = 0
        for a, b in dominoes:
            key = (min(a, b), max(a, b))
            result += count[key]
            count[key] += 1
        return result
