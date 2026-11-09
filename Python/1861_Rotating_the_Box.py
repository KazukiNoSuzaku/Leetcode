# Author: Kaustav Ghosh
# Problem: Rotating the Box
# Approach: Rotating the box clockwise turns its rows into columns and makes gravity pull along each original row towards its right end, so the settling can be done row by row before any rotation happens. Scanning a row from the right with a pointer at the lowest free slot drops each stone exactly where it lands, and meeting an obstacle resets that pointer to just left of it, which is what keeps stones from falling through. The rotation is then a pure reindexing, reading the original grid bottom-to-top to fill each new row.

class Solution(object):
    def rotateTheBox(self, boxGrid):
        """
        :type boxGrid: List[List[str]]
        :rtype: List[List[str]]
        """
        rows, cols = len(boxGrid), len(boxGrid[0])
        settled = [list(row) for row in boxGrid]

        for row in settled:
            free = cols - 1
            for col in range(cols - 1, -1, -1):
                if row[col] == "*":
                    free = col - 1
                elif row[col] == "#":
                    row[col] = "."
                    row[free] = "#"
                    free -= 1

        return [[settled[rows - 1 - step][col] for step in range(rows)]
                for col in range(cols)]
