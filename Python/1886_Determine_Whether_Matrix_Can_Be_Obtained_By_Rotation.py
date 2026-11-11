# Author: Kaustav Ghosh
# Problem: Determine Whether Matrix Can Be Obtained By Rotation
# Approach: Four quarter turns return a matrix to itself, so only four orientations ever need checking and the question is whether any of them equals the target. Each turn is built by reading the rows of the previous orientation bottom to top as columns, which zip over the reversed rows does directly, and the comparison is a plain equality on the nested lists.

class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        current = [list(row) for row in mat]
        wanted = [list(row) for row in target]
        for _ in range(4):
            if current == wanted:
                return True
            current = [list(column) for column in zip(*current[::-1])]
        return False
