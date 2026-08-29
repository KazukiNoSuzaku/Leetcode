# Author: Kaustav Ghosh
# Problem: Remove All Ones With Row and Column Flips II
# Approach: The grid fits in at most 15 cells, so encode it as a bitmask. Each operation picks a set cell and clears its entire row and column. BFS from the initial mask to the all-zero mask gives the minimum number of operations

from collections import deque

class Solution(object):
    def removeOnes(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        clear = [0] * (m * n)
        for r in range(m):
            for c in range(n):
                p = r * n + c
                mask = 0
                for cc in range(n):
                    mask |= 1 << (r * n + cc)
                for rr in range(m):
                    mask |= 1 << (rr * n + c)
                clear[p] = mask

        start = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    start |= 1 << (r * n + c)

        if start == 0:
            return 0
        seen = {start}
        dq = deque([(start, 0)])
        while dq:
            state, steps = dq.popleft()
            p = 0
            s = state
            while s:
                if s & 1:
                    nxt = state & ~clear[p]
                    if nxt == 0:
                        return steps + 1
                    if nxt not in seen:
                        seen.add(nxt)
                        dq.append((nxt, steps + 1))
                s >>= 1
                p += 1
        return 0
