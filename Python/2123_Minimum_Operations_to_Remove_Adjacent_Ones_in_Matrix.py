# Author: Kaustav Ghosh
# Problem: Minimum Operations to Remove Adjacent Ones in Matrix
# Approach: Adjacent 1-cells form edges in a bipartite graph (cells 2-colored by (i+j) parity). Removing the fewest 1s so no two are adjacent is a minimum vertex cover, which by Konig's theorem equals the maximum bipartite matching

class Solution(object):
    def removeOnes(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        graph = {}
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i + j) % 2 == 0:
                    neighbors = []
                    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                            neighbors.append((ni, nj))
                    graph[(i, j)] = neighbors

        match_right = {}

        def augment(u, seen):
            for v in graph[u]:
                if v in seen:
                    continue
                seen.add(v)
                if v not in match_right or augment(match_right[v], seen):
                    match_right[v] = u
                    return True
            return False

        matching = 0
        for u in graph:
            if augment(u, set()):
                matching += 1
        return matching
