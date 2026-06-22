from typing import List

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        INF = float('inf')
        prev = [0] * 10

        for c in range(n):
            freq = [0] * 10
            for r in range(m):
                freq[grid[r][c]] += 1
            cost = [m - freq[d] for d in range(10)]

            sorted_prev = sorted(range(10), key=lambda d: prev[d])
            m1_idx, m2_idx = sorted_prev[0], sorted_prev[1]

            curr = [INF] * 10
            for d in range(10):
                best = prev[m1_idx] if d != m1_idx else prev[m2_idx]
                curr[d] = cost[d] + best
            prev = curr

        return min(prev)
