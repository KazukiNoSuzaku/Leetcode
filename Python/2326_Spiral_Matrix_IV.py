# Author: Kaustav Ghosh
# Problem: 2326. Spiral Matrix IV
# URL: https://leetcode.com/problems/spiral-matrix-iv/
# Difficulty: Medium
#
# Approach:
# Simulate spiral traversal: move right, down, left, up repeatedly.
# Place linked list values in spiral order; fill remaining cells with -1.

class Solution(object):
    def spiralMatrix(self, m, n, head):
        """
        :type m: int
        :type n: int
        :type head: Optional[ListNode]
        :rtype: List[List[int]]
        """
        grid = [[-1] * n for _ in range(m)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0
        r, c = 0, 0

        node = head
        while node:
            grid[r][c] = node.val
            node = node.next

            dr, dc = directions[dir_idx]
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == -1:
                r, c = nr, nc
            else:
                dir_idx = (dir_idx + 1) % 4
                dr, dc = directions[dir_idx]
                r, c = r + dr, c + dc

        return grid
