# Author: Kaustav Ghosh
# Problem: Maximum Matrix Sum
# Approach: Flipping two adjacent signs preserves the parity of negatives, so all magnitudes can be summed. With an even count of negatives every value can be made positive; with an odd count exactly one negative must remain, best placed on the smallest magnitude

class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        total = 0
        negatives = 0
        min_abs = float('inf')
        for row in matrix:
            for v in row:
                total += abs(v)
                if v < 0:
                    negatives += 1
                min_abs = min(min_abs, abs(v))
        if negatives % 2 == 0:
            return total
        return total - 2 * min_abs
