from collections import deque
from sortedcontainers import SortedList

class Solution:
    def minimumVisitedCells(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_avail = [SortedList(range(n)) for _ in range(m)]
        col_avail = [SortedList(range(m)) for _ in range(n)]

        def visit(r: int, c: int) -> None:
            row_avail[r].remove(c)
            col_avail[c].remove(r)

        visit(0, 0)
        queue: deque[tuple[int, int, int]] = deque([(0, 0, 1)])

        while queue:
            r, c, steps = queue.popleft()
            if r == m - 1 and c == n - 1:
                return steps
            reach = grid[r][c]

            to_visit = []
            idx = row_avail[r].bisect_left(c + 1)
            while idx < len(row_avail[r]) and row_avail[r][idx] <= c + reach:
                to_visit.append((r, row_avail[r][idx]))
                idx += 1
            for rr, cc in to_visit:
                visit(rr, cc)
                queue.append((rr, cc, steps + 1))

            to_visit = []
            idx = col_avail[c].bisect_left(r + 1)
            while idx < len(col_avail[c]) and col_avail[c][idx] <= r + reach:
                to_visit.append((col_avail[c][idx], c))
                idx += 1
            for rr, cc in to_visit:
                visit(rr, cc)
                queue.append((rr, cc, steps + 1))

        return -1
