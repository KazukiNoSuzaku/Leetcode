# Simulate a robot navigating with obstacles; find max squared Euclidean distance.

# Author: Kaustav Ghosh

class Solution(object):
    def robotSim(self, commands, obstacles):
        obstacle_set = set(map(tuple, obstacles))
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        d = x = y = 0
        res = 0
        for cmd in commands:
            if cmd == -2: d = (d - 1) % 4
            elif cmd == -1: d = (d + 1) % 4
            else:
                for _ in range(cmd):
                    nx, ny = x + dirs[d][0], y + dirs[d][1]
                    if (nx, ny) not in obstacle_set:
                        x, y = nx, ny
                        res = max(res, x*x + y*y)
        return res
