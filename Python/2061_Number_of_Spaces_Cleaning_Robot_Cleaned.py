# Author: Kaustav Ghosh
# Problem: Number of Spaces Cleaning Robot Cleaned
# Approach: Simulate the robot: clean the current cell, move forward if the next cell is free, otherwise turn right. The path is deterministic and eventually repeats, so stop when a (cell, direction) state recurs and count the distinct cleaned cells

class Solution(object):
    def numberOfCleanRooms(self, room):
        """
        :type room: List[List[int]]
        :rtype: int
        """
        m, n = len(room), len(room[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        seen = set()
        cleaned = set()
        r = c = d = 0
        while (r, c, d) not in seen:
            seen.add((r, c, d))
            cleaned.add((r, c))
            dr, dc = dirs[d]
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and room[nr][nc] == 0:
                r, c = nr, nc
            else:
                d = (d + 1) % 4
        return len(cleaned)
