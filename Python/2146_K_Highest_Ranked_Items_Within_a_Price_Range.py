# Author: Kaustav Ghosh
# Problem: K Highest Ranked Items Within a Price Range
# Approach: BFS from the start over walkable cells to get each item's shortest distance. Collect items whose price is within the range and rank them by (distance, price, row, column); return the top k positions

from collections import deque

class Solution(object):
    def highestRankedKItems(self, grid, pricing, start, k):
        """
        :type grid: List[List[int]]
        :type pricing: List[int]
        :type start: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        low, high = pricing
        sr, sc = start
        seen = [[False] * n for _ in range(m)]
        seen[sr][sc] = True
        dq = deque([(sr, sc, 0)])
        items = []
        while dq:
            r, c, d = dq.popleft()
            price = grid[r][c]
            if price >= 2 and low <= price <= high:
                items.append((d, price, r, c))
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not seen[nr][nc] and grid[nr][nc] != 0:
                    seen[nr][nc] = True
                    dq.append((nr, nc, d + 1))

        items.sort()
        return [[r, c] for _, _, r, c in items[:k]]
