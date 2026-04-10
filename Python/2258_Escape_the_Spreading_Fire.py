# Author: Kaustav Ghosh
# Problem: 2258. Escape the Spreading Fire
# URL: https://leetcode.com/problems/escape-the-spreading-fire/
# Difficulty: Hard
#
# Approach:
# Binary search on the number of minutes to wait. BFS from all fire cells
# to compute fire arrival times. Then BFS from (0,0) with a time offset
# to check if we can reach (m-1, n-1) before or at the same time as fire.

from collections import deque

class Solution(object):
    def maximumMinutes(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        INF = float('inf')

        # BFS to compute fire arrival time at each cell
        fire_time = [[INF] * n for _ in range(m)]
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fire_time[i][j] = 0
                    q.append((i, j))
        while q:
            r, c = q.popleft()
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 2 and fire_time[nr][nc] == INF:
                    fire_time[nr][nc] = fire_time[r][c] + 1
                    q.append((nr, nc))

        def can_escape(wait):
            visited = [[False] * n for _ in range(m)]
            if wait >= fire_time[0][0]:
                return False
            visited[0][0] = True
            q = deque()
            q.append((0, 0, wait))
            while q:
                r, c, t = q.popleft()
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    nt = t + 1
                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] != 2:
                        if nr == m - 1 and nc == n - 1:
                            if nt <= fire_time[nr][nc]:
                                return True
                        elif nt < fire_time[nr][nc]:
                            visited[nr][nc] = True
                            q.append((nr, nc, nt))
            return False

        lo, hi = 0, m * n
        if not can_escape(0):
            return -1
        if can_escape(hi):
            return 10 ** 9
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can_escape(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
