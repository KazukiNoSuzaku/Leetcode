# Author: Kaustav Ghosh
# Prefix sum matrix with binary search on side length

class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        m, n = len(mat), len(mat[0])
        # Build prefix sum
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = mat[i - 1][j - 1] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]

        def get_sum(r1, c1, r2, c2):
            return prefix[r2 + 1][c2 + 1] - prefix[r1][c2 + 1] - prefix[r2 + 1][c1] + prefix[r1][c1]

        result = 0
        for i in range(m):
            for j in range(n):
                # Try to extend from current best
                side = result + 1
                while i + side <= m and j + side <= n:
                    if get_sum(i, j, i + side - 1, j + side - 1) <= threshold:
                        result = side
                        side += 1
                    else:
                        break
        return result
