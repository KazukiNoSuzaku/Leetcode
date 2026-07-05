# Author: Kaustav Ghosh
# Problem: Path With Minimum Effort
# Approach: Dijkstra where a path's cost is the max step difference along it; relax neighbors by the larger of current effort and the edge height gap

import heapq

class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        R, C = len(heights), len(heights[0])
        effort = [[float('inf')] * C for _ in range(R)]
        effort[0][0] = 0
        pq = [(0, 0, 0)]  # (effort so far, row, col)

        while pq:
            e, r, c = heapq.heappop(pq)
            if r == R - 1 and c == C - 1:
                return e
            if e > effort[r][c]:
                continue
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C:
                    ne = max(e, abs(heights[nr][nc] - heights[r][c]))
                    if ne < effort[nr][nc]:
                        effort[nr][nc] = ne
                        heapq.heappush(pq, (ne, nr, nc))
        return 0
