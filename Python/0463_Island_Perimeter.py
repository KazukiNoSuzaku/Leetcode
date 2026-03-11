# You are given row x col grid representing a map where grid[i][j] = 1 represents land
# and grid[i][j] = 0 represents water.
# Return the perimeter of the island.

# Author: Kaustav Ghosh

class Solution(object):
    def islandPerimeter(self, grid):
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 2
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 2
        return perimeter
