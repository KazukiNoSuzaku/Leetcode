# Author: Kaustav Ghosh
# Problem: 1591 - Strange Printer II
# Approach: Topological sort on color overlap dependencies

from collections import defaultdict, deque

class Solution(object):
    def isPrintable(self, targetGrid):
        """
        :type targetGrid: List[List[int]]
        :rtype: bool
        """
        rows, cols = len(targetGrid), len(targetGrid[0])
        # Find bounding box for each color
        bbox = {}
        for r in range(rows):
            for c in range(cols):
                color = targetGrid[r][c]
                if color not in bbox:
                    bbox[color] = [r, c, r, c]
                else:
                    bbox[color][0] = min(bbox[color][0], r)
                    bbox[color][1] = min(bbox[color][1], c)
                    bbox[color][2] = max(bbox[color][2], r)
                    bbox[color][3] = max(bbox[color][3], c)

        # Build dependency graph: color A depends on color B if B appears inside A's bbox
        graph = defaultdict(set)
        in_degree = {color: 0 for color in bbox}

        for color, (r1, c1, r2, c2) in bbox.items():
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    other = targetGrid[r][c]
                    if other != color and other not in graph[color]:
                        graph[color].add(other)
                        in_degree[other] = in_degree.get(other, 0) + 1

        # Topological sort
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        processed = 0
        while queue:
            color = queue.popleft()
            processed += 1
            for dep in graph[color]:
                in_degree[dep] -= 1
                if in_degree[dep] == 0:
                    queue.append(dep)

        return processed == len(bbox)
