# Author: Kaustav Ghosh
# Problem: Last Day Where You Can Still Cross
# Approach: Crossing is monotonic - if a top-to-bottom land path survives on day d it also survives earlier. Binary search the day; for a candidate flood the first d cells and BFS from the top row through remaining land to see if the bottom row is reachable

from collections import deque

class Solution(object):
    def latestDayToCross(self, row, col, cells):
        """
        :type row: int
        :type col: int
        :type cells: List[List[int]]
        :rtype: int
        """
        def can_cross(day):
            water = [[False] * col for _ in range(row)]
            for i in range(day):
                r, c = cells[i]
                water[r - 1][c - 1] = True
            vis = [[False] * col for _ in range(row)]
            dq = deque()
            for c in range(col):
                if not water[0][c]:
                    vis[0][c] = True
                    dq.append((0, c))
            while dq:
                r, c = dq.popleft()
                if r == row - 1:
                    return True
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and not vis[nr][nc] and not water[nr][nc]:
                        vis[nr][nc] = True
                        dq.append((nr, nc))
            return False

        lo, hi, ans = 1, row * col, 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_cross(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
