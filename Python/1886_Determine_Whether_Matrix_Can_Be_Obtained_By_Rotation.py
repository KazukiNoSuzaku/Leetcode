# Author: Kaustav Ghosh
# Problem: Determine Whether Matrix Can Be Obtained By Rotation
# Approach: Rotate mat 90 degrees clockwise up to three times, checking after each whether it matches target

class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        def rotate(m):
            return [list(row) for row in zip(*m[::-1])]

        for _ in range(4):
            if mat == target:
                return True
            mat = rotate(mat)
        return False
