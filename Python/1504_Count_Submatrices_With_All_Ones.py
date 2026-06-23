# Author: Kaustav Ghosh
# Problem: Count Submatrices With All Ones
# Approach: For each row build height histogram; for each cell scan left tracking min height to count rectangles

class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m, n = len(mat), len(mat[0])
        heights = [0] * n
        ans = 0
        for row in mat:
            for j in range(n):
                heights[j] = heights[j] + 1 if row[j] == 1 else 0
            for j in range(n):
                min_h = heights[j]
                for k in range(j, -1, -1):
                    min_h = min(min_h, heights[k])
                    ans += min_h
        return ans
