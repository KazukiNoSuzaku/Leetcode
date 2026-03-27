# Author: Kaustav Ghosh
# https://leetcode.com/problems/k-highest-ranked-items-within-a-price-range/

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
        visited = [[False] * n for _ in range(m)]
        visited[sr][sc] = True
        queue = deque([(0, sr, sc)])
        items = []

        while queue:
            dist, r, c = queue.popleft()
            price = grid[r][c]
            if low <= price <= high:
                items.append((dist, price, r, c))
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] != 0:
                    visited[nr][nc] = True
                    queue.append((dist + 1, nr, nc))

        items.sort()
        return [[r, c] for _, _, r, c in items[:k]]
