# Author: Kaustav Ghosh
# Problem: Find Kth Largest XOR Coordinate Value
# Approach: The value at a coordinate is the exclusive-or over the whole rectangle above and to the left of it, and that obeys the same inclusion-exclusion shape as a two-dimensional prefix sum, except that exclusive-or is its own inverse so the doubly-counted corner is applied once more rather than subtracted. Building the table in place therefore gives every coordinate's value in a single pass, after which the answer is the k-th largest of those values; a bounded heap of size k keeps only the candidates that could still matter, which costs less memory than sorting the whole table when k is small.

from heapq import heappush, heappushpop


class Solution(object):
    def kthLargestValue(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        rows, cols = len(matrix), len(matrix[0])
        best = []
        for r in range(rows):
            row = matrix[r]
            above = matrix[r - 1] if r else None
            for c in range(cols):
                value = row[c]
                if c:
                    value ^= row[c - 1]
                if above is not None:
                    value ^= above[c]
                    if c:
                        # Exclusive-or undoes itself, so the overlap comes back in.
                        value ^= above[c - 1]
                row[c] = value
                if len(best) < k:
                    heappush(best, value)
                elif value > best[0]:
                    heappushpop(best, value)
        return best[0]
