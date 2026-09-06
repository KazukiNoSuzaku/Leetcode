# Author: Kaustav Ghosh
# Problem: Escape the Spreading Fire
# Approach: Precompute, via multi-source BFS, the minute the fire reaches each cell. For a chosen wait time the person's arrival time at each cell is fixed by BFS from the start; a move is safe if the person arrives strictly before the fire, except the safehouse where arriving at the same minute still counts. Binary search the largest feasible wait; all-feasible means 1e9, wait 0 infeasible means -1

from collections import deque


class Solution(object):
    def maximumMinutes(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        INF = float('inf')
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        # fire arrival time per cell
        fire_time = [[INF] * n for _ in range(m)]
        q = deque()
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fire_time[r][c] = 0
                    q.append((r, c))
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 0 and fire_time[nr][nc] == INF:
                    fire_time[nr][nc] = fire_time[r][c] + 1
                    q.append((nr, nc))

        def feasible(wait):
            if fire_time[0][0] <= wait:
                return False
            arrival = [[INF] * n for _ in range(m)]
            arrival[0][0] = wait
            dq = deque([(0, 0)])
            while dq:
                r, c = dq.popleft()
                t = arrival[r][c] + 1
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue
                    if grid[nr][nc] == 2 or arrival[nr][nc] != INF:
                        continue
                    if nr == m - 1 and nc == n - 1:
                        if t <= fire_time[nr][nc]:
                            return True
                        continue
                    if t < fire_time[nr][nc]:
                        arrival[nr][nc] = t
                        dq.append((nr, nc))
            return False

        limit = m * n
        if feasible(limit):
            return 10 ** 9
        if not feasible(0):
            return -1
        lo, hi = 0, limit
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if feasible(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
