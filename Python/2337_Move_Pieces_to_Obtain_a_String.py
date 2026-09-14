# Author: Kaustav Ghosh
# Problem: Move Pieces to Obtain a String
# Approach: Pieces can never pass each other, so the L/R sequences with blanks removed must match exactly. Pair the pieces in order with two pointers: an L only moves left, so its start index must be >= its target index; an R only moves right, so its start index must be <= its target index

class Solution(object):
    def canChange(self, start, target):
        """
        :type start: str
        :type target: str
        :rtype: bool
        """
        n = len(start)
        i = j = 0
        while True:
            while i < n and start[i] == '_':
                i += 1
            while j < n and target[j] == '_':
                j += 1
            if i == n or j == n:
                return i == n and j == n
            if start[i] != target[j]:
                return False
            if start[i] == 'L' and i < j:
                return False
            if start[i] == 'R' and i > j:
                return False
            i += 1
            j += 1
