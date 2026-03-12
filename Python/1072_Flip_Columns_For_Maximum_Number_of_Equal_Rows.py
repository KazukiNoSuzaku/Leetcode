# Author: Kaustav Ghosh
# 1072. Flip Columns For Maximum Number of Equal Rows
# https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/

from collections import Counter

class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        count = Counter()
        for row in matrix:
            # Normalize: if row[0]==1 flip all, so canonical form starts with 0
            key = tuple(v ^ row[0] for v in row)
            count[key] += 1
        return max(count.values())
