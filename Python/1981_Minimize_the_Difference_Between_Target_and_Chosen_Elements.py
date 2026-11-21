# Author: Kaustav Ghosh
# Problem: Minimize the Difference Between Target and Chosen Elements
# Approach: Only the running total matters, not which element produced it, so I track the set of totals reachable after each row and read the answer off the final set. The grid is at most 70 by 70 with entries at most 70, so no total can exceed 4900 and the whole reachable set fits in the bits of one integer: bit s set means total s is reachable. Each row then costs one shift and one bitwise or per distinct value in it, which pushes all the work into Python's big-integer arithmetic instead of a Python-level loop over totals, and duplicates within a row are collapsed by taking the row's distinct values. At the end I scan the bits once and keep the smallest distance to the target. That is O(m * n) big-integer operations on a 4901-bit word.

class Solution(object):
    def minimizeTheDifference(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: int
        :rtype: int
        """
        reachable = 1
        for row in mat:
            shifted = 0
            for value in set(row):
                shifted |= reachable << value
            reachable = shifted

        best = None
        total = 0
        while reachable:
            if reachable & 1:
                gap = abs(total - target)
                if best is None or gap < best:
                    best = gap
            reachable >>= 1
            total += 1
        return best
