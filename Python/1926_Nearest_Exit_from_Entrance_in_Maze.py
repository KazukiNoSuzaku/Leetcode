# Author: Kaustav Ghosh
# Problem: Nearest Exit from Entrance in Maze
# Approach: Every step costs the same, so a breadth-first sweep from the entrance reaches each cell by the fewest steps and the first border cell it reaches is the nearest exit. The entrance itself sits on the border but does not count, which is handled by testing for an exit only on cells the search moves into rather than on the cell it starts from. Cells are marked as walls the moment they are queued, so none is enqueued twice and the sweep stays linear in the grid.

class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        from collections import deque

        rows, cols = len(maze), len(maze[0])
        seen = [[cell == "+" for cell in row] for row in maze]
        start = (entrance[0], entrance[1])
        seen[start[0]][start[1]] = True

        queue = deque([start])
        steps = 0
        while queue:
            steps += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if not (0 <= nr < rows and 0 <= nc < cols) or seen[nr][nc]:
                        continue
                    if nr in (0, rows - 1) or nc in (0, cols - 1):
                        return steps
                    seen[nr][nc] = True
                    queue.append((nr, nc))
        return -1
