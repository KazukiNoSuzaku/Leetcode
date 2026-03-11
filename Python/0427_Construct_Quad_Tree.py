# Given a n * n matrix grid of 0's and 1's, we want to represent grid with a Quad-Tree.
# Return the root of the Quad-Tree representing grid.

# Author: Kaustav Ghosh

class Solution(object):
    def construct(self, grid):
        def build(r, c, size):
            val = grid[r][c]
            leaf = all(grid[r+i][c+j] == val for i in range(size) for j in range(size))
            if leaf:
                return Node(val, True, None, None, None, None)
            half = size // 2
            return Node(
                1, False,
                build(r, c, half),
                build(r, c + half, half),
                build(r + half, c, half),
                build(r + half, c + half, half)
            )
        return build(0, 0, len(grid))
