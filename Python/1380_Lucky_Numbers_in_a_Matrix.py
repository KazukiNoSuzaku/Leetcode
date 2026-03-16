# Author: Kaustav Ghosh
# Problem: Lucky Numbers in a Matrix
# Approach: Find numbers that are row minimum and column maximum

class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        row_mins = {min(row) for row in matrix}
        col_maxs = {max(col) for col in zip(*matrix)}
        return list(row_mins & col_maxs)
