# Given n points on a 2D plane, find if there is a line parallel to the y-axis
# that reflects the given set of points symmetrically.
# In other words, answer whether or not if there exists a line that after reflecting
# all points over the given line, the original points' set is the same as the reflected ones.

# Example 1:
# Input: points = [[1,1],[-1,1]]
# Output: true

# Example 2:
# Input: points = [[1,1],[-1,-1]]
# Output: false

# Constraints:
# n == points.length
# 1 <= n <= 10^4
# -10^8 <= points[i][j] <= 10^8

# Author: Kaustav Ghosh

class Solution(object):
    def isReflected(self, points):
        point_set = set(map(tuple, points))
        min_x = min(p[0] for p in points)
        max_x = max(p[0] for p in points)
        total = min_x + max_x
        for x, y in points:
            if (total - x, y) not in point_set:
                return False
        return True
