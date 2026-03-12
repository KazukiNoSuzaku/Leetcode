# Author: Kaustav Ghosh
# Track row and column increments, count cells with odd total

class Solution(object):
    def oddCells(self, m, n, indices):
        """
        :type m: int
        :type n: int
        :type indices: List[List[int]]
        :rtype: int
        """
        rows = [0] * m
        cols = [0] * n
        for r, c in indices:
            rows[r] += 1
            cols[c] += 1
        count = 0
        for i in range(m):
            for j in range(n):
                if (rows[i] + cols[j]) % 2 == 1:
                    count += 1
        return count
