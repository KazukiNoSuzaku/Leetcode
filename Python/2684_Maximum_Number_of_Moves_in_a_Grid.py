class Solution:
    def maxMoves(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        reachable = set(range(m))
        for c in range(n - 1):
            nxt = set()
            for r in reachable:
                for dr in (-1, 0, 1):
                    nr = r + dr
                    if 0 <= nr < m and grid[nr][c + 1] > grid[r][c]:
                        nxt.add(nr)
            if not nxt:
                return c
            reachable = nxt
        return n - 1
