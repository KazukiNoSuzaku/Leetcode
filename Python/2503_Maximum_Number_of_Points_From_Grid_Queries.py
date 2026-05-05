import heapq

class Solution:
    def maxPoints(self, grid: list[list[int]], queries: list[int]) -> list[int]:
        # Sort queries offline; BFS via min-heap expanding cells < current threshold.
        m, n = len(grid), len(grid[0])
        ans = [0] * len(queries)
        heap = [(grid[0][0], 0, 0)]
        vis = {(0, 0)}
        count = 0
        for qi, q in sorted(enumerate(queries), key=lambda x: x[1]):
            while heap and heap[0][0] < q:
                v, r, c = heapq.heappop(heap)
                count += 1
                for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in vis:
                        vis.add((nr, nc))
                        heapq.heappush(heap, (grid[nr][nc], nr, nc))
            ans[qi] = count
        return ans
