# Author: Kaustav Ghosh
# Problem: Subrectangle Queries
# Approach: Store updates list, brute force latest value lookup

class Solution(object):
    pass

class SubrectangleQueries(object):

    def __init__(self, rectangle):
        """
        :type rectangle: List[List[int]]
        """
        self.rect = rectangle
        self.updates = []

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :type newValue: int
        :rtype: None
        """
        self.updates.append((row1, col1, row2, col2, newValue))

    def getValue(self, row, col):
        """
        :type row: int
        :type col: int
        :rtype: int
        """
        for r1, c1, r2, c2, val in reversed(self.updates):
            if r1 <= row <= r2 and c1 <= col <= c2:
                return val
        return self.rect[row][col]
