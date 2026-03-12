# Author: Kaustav Ghosh
# 1041. Robot Bounded In Circle
# https://leetcode.com/problems/robot-bounded-in-circle/

class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        x, y = 0, 0
        # directions: north, east, south, west
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        for c in instructions:
            if c == 'G':
                x += dirs[d][0]
                y += dirs[d][1]
            elif c == 'L':
                d = (d - 1) % 4
            else:
                d = (d + 1) % 4
        # bounded if back at origin or not facing north
        return (x == 0 and y == 0) or d != 0
