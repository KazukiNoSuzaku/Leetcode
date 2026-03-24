# Author: Kaustav Ghosh
# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        n = len(mat)
        for _ in range(4):
            if mat == target:
                return True
            # Rotate 90 degrees clockwise
            mat = [[mat[n - 1 - j][i] for j in range(n)] for i in range(n)]
        return False
