# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean.
# Water can only flow in four directions and flow to a neighboring cell only if its height
# is less than or equal to the current cell's height.
# Return a 2D list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

# Author: Kaustav Ghosh

from collections import deque

class Solution(object):
    def pacificAtlantic(self, heights):
        m, n = len(heights), len(heights[0])
        def bfs(starts):
            visited = set(starts)
            queue = deque(starts)
            while queue:
                r, c = queue.popleft()
                for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return visited
        pacific = [(0, j) for j in range(n)] + [(i, 0) for i in range(1, m)]
        atlantic = [(m-1, j) for j in range(n)] + [(i, n-1) for i in range(m-1)]
        return list(bfs(pacific) & bfs(atlantic))
