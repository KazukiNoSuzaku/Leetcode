# There is a ball in a maze. Find the shortest path for the ball to drop into the hole.
# Among all shortest paths, return the lexicographically smallest one. Return "impossible" if none.

# Author: Kaustav Ghosh

import heapq

class Solution(object):
    def findShortestWay(self, maze, ball, hole):
        m, n = len(maze), len(maze[0])
        dist = {(ball[0], ball[1]): (0, '')}
        heap = [(0, '', ball[0], ball[1])]
        dirs = [('d', 1, 0), ('l', 0, -1), ('r', 0, 1), ('u', -1, 0)]
        while heap:
            d, path, r, c = heapq.heappop(heap)
            if [r, c] == hole:
                return path
            if (d, path) > dist.get((r, c), (float('inf'), '')):
                continue
            for name, dr, dc in dirs:
                nr, nc, steps = r, c, 0
                while 0 <= nr+dr < m and 0 <= nc+dc < n and maze[nr+dr][nc+dc] == 0:
                    nr += dr; nc += dc; steps += 1
                    if [nr, nc] == hole: break
                nd, np = d + steps, path + name
                if (nd, np) < dist.get((nr, nc), (float('inf'), '')):
                    dist[(nr, nc)] = (nd, np)
                    heapq.heappush(heap, (nd, np, nr, nc))
        return 'impossible'
