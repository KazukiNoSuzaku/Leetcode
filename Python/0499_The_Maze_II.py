# There is a ball in a maze. The ball can roll through empty spaces but won't stop rolling
# until hitting a wall. Return the shortest distance for the ball to stop at the destination.
# If the ball cannot stop at destination, return -1.

# Author: Kaustav Ghosh

import heapq

class Solution(object):
    def shortestDistance(self, maze, start, destination):
        m, n = len(maze), len(maze[0])
        dist = [[float('inf')] * n for _ in range(m)]
        dist[start[0]][start[1]] = 0
        heap = [(0, start[0], start[1])]
        while heap:
            d, r, c = heapq.heappop(heap)
            if d > dist[r][c]:
                continue
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc, steps = r, c, 0
                while 0 <= nr + dr < m and 0 <= nc + dc < n and maze[nr+dr][nc+dc] == 0:
                    nr += dr
                    nc += dc
                    steps += 1
                if dist[r][c] + steps < dist[nr][nc]:
                    dist[nr][nc] = dist[r][c] + steps
                    heapq.heappush(heap, (dist[nr][nc], nr, nc))
        res = dist[destination[0]][destination[1]]
        return res if res != float('inf') else -1
