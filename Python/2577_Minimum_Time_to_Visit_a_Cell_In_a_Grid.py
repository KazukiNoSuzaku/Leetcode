import heapq

class Solution:
    def minimumTime(self, grid: list[list[int]]) -> int:
        # If both first neighbors require time > 1, we can't bounce out of (0,0) → impossible.
        m, n = len(grid), len(grid[0])
        if m > 1 and n > 1 and grid[1][0] > 1 and grid[0][1] > 1:
            return -1

        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        heap = [(0, 0, 0)]
        while heap:
            t, r, c = heapq.heappop(heap)
            if r == m - 1 and c == n - 1:
                return t
            if t > dist[r][c]:
                continue
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    nt = max(t + 1, grid[nr][nc])
                    if (nt - t) % 2 == 0:
                        nt += 1  # parity fix: bounce to wait an extra step
                    if nt < dist[nr][nc]:
                        dist[nr][nc] = nt
                        heapq.heappush(heap, (nt, nr, nc))
        return -1
