# Author: Kaustav Ghosh
# Problem: Maximum Number of Points From Grid Queries
# Approach: A bigger query reaches everything a smaller one does, so answer the queries in increasing order and never restart the walk. A min-heap of frontier cells keyed by value lets each query simply keep absorbing cells below its threshold, and the running count of absorbed cells is its answer

import heapq


class Solution(object):
    def maxPoints(self, grid, queries):
        """
        :type grid: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        rows, cols = len(grid), len(grid[0])
        answer = [0] * len(queries)
        frontier = [(grid[0][0], 0, 0)]
        seen = [[False] * cols for _ in range(rows)]
        seen[0][0] = True
        points = 0
        for query, index in sorted((q, i) for i, q in enumerate(queries)):
            while frontier and frontier[0][0] < query:
                _, r, c = heapq.heappop(frontier)
                points += 1
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if 0 <= nr < rows and 0 <= nc < cols and not seen[nr][nc]:
                        seen[nr][nc] = True
                        heapq.heappush(frontier, (grid[nr][nc], nr, nc))
            answer[index] = points
        return answer
