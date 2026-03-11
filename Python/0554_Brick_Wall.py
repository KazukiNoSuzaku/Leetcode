# There is a rectangular brick wall in front of you with n rows of bricks. The bricks have the
# same height but different width. Return the minimum number of bricks crossed when drawing
# a vertical line from top to bottom.

# Author: Kaustav Ghosh

from collections import Counter

class Solution(object):
    def leastBricks(self, wall):
        edge_count = Counter()
        for row in wall:
            pos = 0
            for brick in row[:-1]:
                pos += brick
                edge_count[pos] += 1
        return len(wall) - max(edge_count.values() or [0])
