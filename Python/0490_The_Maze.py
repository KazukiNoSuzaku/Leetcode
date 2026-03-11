# There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1).
# The ball can roll up, down, left or right through empty spaces but it won't stop rolling
# until hitting a wall. Return true if the ball can stop at the destination.

# Author: Kaustav Ghosh

from collections import deque

class Solution(object):
    def hasPath(self, maze, start, destination):
        m, n = len(maze), len(maze[0])
        visited = set()
        queue = deque([tuple(start)])
        visited.add(tuple(start))
        while queue:
            r, c = queue.popleft()
            if [r, c] == destination:
                return True
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r, c
                while 0 <= nr + dr < m and 0 <= nc + dc < n and maze[nr+dr][nc+dc] == 0:
                    nr += dr
                    nc += dc
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        return False
