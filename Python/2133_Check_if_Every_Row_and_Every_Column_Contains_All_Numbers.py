# Author: Kaustav Ghosh
# https://leetcode.com/problems/check-if-every-row-and-every-column-contains-all-numbers/

class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n = len(matrix)
        for i in range(n):
            if len(set(matrix[i])) != n:
                return False
            if len(set(matrix[j][i] for j in range(n))) != n:
                return False
        return True
