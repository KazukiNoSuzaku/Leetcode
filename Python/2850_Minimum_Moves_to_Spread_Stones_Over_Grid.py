from typing import List
from itertools import permutations

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        sources, destinations = [], []
        for r in range(3):
            for c in range(3):
                if grid[r][c] > 1:
                    sources.extend([(r, c)] * (grid[r][c] - 1))
                elif grid[r][c] == 0:
                    destinations.append((r, c))

        res = float('inf')
        for perm in permutations(range(len(destinations))):
            cost = sum(
                abs(sources[i][0] - destinations[perm[i]][0]) + abs(sources[i][1] - destinations[perm[i]][1])
                for i in range(len(sources))
            )
            res = min(res, cost)
        return res
