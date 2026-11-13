# Author: Kaustav Ghosh
# Problem: Count Sub Islands
# Approach: An island of the second grid qualifies only if every one of its cells is also land in the first, so each island is flooded in full and a single flag records whether any cell broke that condition; stopping early would leave part of the island unvisited and let it be counted again from another starting cell. The flood is an explicit stack rather than recursion, because a five hundred by five hundred grid of solid land is one island a quarter of a million cells deep. Visited cells are marked in a copy of the second grid, so the caller's grids are untouched.

class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid2), len(grid2[0])
        remaining = [list(row) for row in grid2]

        islands = 0
        for start_row in range(rows):
            for start_col in range(cols):
                if not remaining[start_row][start_col]:
                    continue
                remaining[start_row][start_col] = 0
                stack = [(start_row, start_col)]
                contained = True
                while stack:
                    r, c = stack.pop()
                    if not grid1[r][c]:
                        contained = False
                    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                        if 0 <= nr < rows and 0 <= nc < cols and remaining[nr][nc]:
                            remaining[nr][nc] = 0
                            stack.append((nr, nc))
                if contained:
                    islands += 1
        return islands
