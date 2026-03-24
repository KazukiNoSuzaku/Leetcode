# Author: Kaustav Ghosh
# https://leetcode.com/problems/last-day-where-you-can-still-cross/

class Solution(object):
    def latestDayToCross(self, row, col, cells):
        """
        :type row: int
        :type col: int
        :type cells: List[List[int]]
        :rtype: int
        """
        # Binary search on the day
        def canCross(day):
            grid = [[0] * col for _ in range(row)]
            for i in range(day):
                r, c = cells[i]
                grid[r - 1][c - 1] = 1  # water
            # BFS from top row to bottom row
            from collections import deque
            q = deque()
            for c in range(col):
                if grid[0][c] == 0:
                    q.append((0, c))
                    grid[0][c] = 1
            while q:
                r, c = q.popleft()
                if r == row - 1:
                    return True
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        q.append((nr, nc))
            return False

        lo, hi = 1, len(cells)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if canCross(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
