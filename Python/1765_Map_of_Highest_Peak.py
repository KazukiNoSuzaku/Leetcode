# Author: Kaustav Ghosh
# Problem: Map of Highest Peak
# Approach: Water cells are height 0; a multi-source BFS from all of them assigns each land cell its distance to the nearest water, which is the maximal valid height

from collections import deque

class Solution(object):
    def highestPeak(self, isWater):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = len(isWater), len(isWater[0])
        height = [[-1] * cols for _ in range(rows)]
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if isWater[r][c] == 1:
                    height[r][c] = 0
                    queue.append((r, c))

        while queue:
            r, c = queue.popleft()
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and height[nr][nc] == -1:
                    height[nr][nc] = height[r][c] + 1
                    queue.append((nr, nc))

        return height
