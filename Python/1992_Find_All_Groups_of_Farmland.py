# Author: Kaustav Ghosh
# Problem: Find All Groups of Farmland
# Approach: Every group is guaranteed to be a solid rectangle separated from the others, so no flood fill is needed at all. A cell is the top-left corner of a group exactly when it holds farmland and the cells immediately above and to its left are hay or off the grid; from such a corner the rectangle's extent is found by walking right while the row stays farmland and down while the column stays farmland. That walk visits each cell of the rectangle's first row and first column only, so the whole scan stays linear in the grid.

class Solution(object):
    def findFarmland(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(land)
        columns = len(land[0])
        groups = []
        for row in range(rows):
            for column in range(columns):
                if land[row][column] == 0:
                    continue
                if row > 0 and land[row - 1][column] == 1:
                    continue
                if column > 0 and land[row][column - 1] == 1:
                    continue
                last_column = column
                while last_column + 1 < columns and land[row][last_column + 1] == 1:
                    last_column += 1
                last_row = row
                while last_row + 1 < rows and land[last_row + 1][column] == 1:
                    last_row += 1
                groups.append([row, column, last_row, last_column])
        return groups
