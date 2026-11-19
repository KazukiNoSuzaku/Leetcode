# Author: Kaustav Ghosh
# Problem: Last Day Where You Can Still Cross
# Approach: Crossing is monotone in time: once a path from top to bottom is gone, later flooding only removes more land, so the set of days on which a crossing exists is a prefix and the last of them can be found by binary search on the day. Testing a single day means flooding the first d cells and asking whether any top-row land cell reaches the bottom row through land in the four directions, which is one breadth-first search with an explicit queue; I mark cells as visited in the same grid used for the water so no second structure is needed per probe. The grid holds at most 2 * 10^4 cells, so each probe is linear in that and the whole search costs O(row * col * log(row * col)).

class Solution(object):
    def latestDayToCross(self, row, col, cells):
        """
        :type row: int
        :type col: int
        :type cells: List[List[int]]
        :rtype: int
        """
        def crossable(day):
            flooded = [[False] * col for _ in range(row)]
            for index in range(day):
                r, c = cells[index]
                flooded[r - 1][c - 1] = True

            queue = []
            for c in range(col):
                if not flooded[0][c]:
                    flooded[0][c] = True
                    queue.append((0, c))
            if row == 1:
                return bool(queue)

            while queue:
                nxt = []
                for r, c in queue:
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < row and 0 <= nc < col and not flooded[nr][nc]:
                            if nr == row - 1:
                                return True
                            flooded[nr][nc] = True
                            nxt.append((nr, nc))
                queue = nxt
            return False

        low, high = 1, len(cells)
        while low < high:
            middle = (low + high + 1) // 2
            if crossable(middle):
                low = middle
            else:
                high = middle - 1
        return low
