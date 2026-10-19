# Author: Kaustav Ghosh
# Problem: Path With Minimum Effort
# Approach: The cost of a route is the largest single step on it rather than a sum, so the usual shortest-path arithmetic does not apply, but Dijkstra's method still does once "distance" is redefined as the worst step taken so far: extending a route replaces that worst value with the larger of it and the new step, which is still monotone, so the first time a cell is finalised it holds the best possible worst step. A heap keyed on that value therefore settles the grid in one sweep, with no need to guess a threshold and test it.

from heapq import heappush, heappop


class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        rows, cols = len(heights), len(heights[0])
        if rows == 1 and cols == 1:
            return 0
        worst = [[-1] * cols for _ in range(rows)]
        queue = [(0, 0, 0)]
        while queue:
            effort, r, c = heappop(queue)
            if worst[r][c] != -1:
                continue
            worst[r][c] = effort
            if r == rows - 1 and c == cols - 1:
                return effort
            here = heights[r][c]
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < rows and 0 <= nc < cols and worst[nr][nc] == -1:
                    step = abs(heights[nr][nc] - here)
                    heappush(queue, (effort if effort > step else step, nr, nc))
        return 0
