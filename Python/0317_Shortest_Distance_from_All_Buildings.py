# You are given an m x n grid grid of values 0, 1, or 2, where:
# - 0 represents an empty land that you can pass by freely,
# - 1 represents a building that you cannot pass through,
# - 2 represents an obstacle that you cannot pass through.
# You want to build a house on an empty land that reaches all buildings in the shortest total travel
# distance. Return this shortest distance or -1 if it is not possible.

# Example 1:
# Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
# Output: 7

# Constraints:
# m == grid.length, n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0, 1, or 2.

# Author: Kaustav Ghosh

from collections import deque

class Solution(object):
    def shortestDistance(self, grid):
        m, n = len(grid), len(grid[0])
        dist = [[0] * n for _ in range(m)]
        reach = [[0] * n for _ in range(m)]
        buildings = sum(grid[i][j] == 1 for i in range(m) for j in range(n))

        def bfs(sr, sc):
            visited = [[False] * n for _ in range(m)]
            visited[sr][sc] = True
            q = deque([(sr, sc, 0)])
            while q:
                r, c, d = q.popleft()
                for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == 0:
                        visited[nr][nc] = True
                        dist[nr][nc] += d + 1
                        reach[nr][nc] += 1
                        q.append((nr, nc, d + 1))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs(i, j)

        res = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and reach[i][j] == buildings:
                    res = min(res, dist[i][j])
        return -1 if res == float('inf') else res
