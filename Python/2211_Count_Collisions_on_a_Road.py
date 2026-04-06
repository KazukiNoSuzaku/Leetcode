# Author: Kaustav Ghosh
# Problem: 2211. Count Collisions on a Road
# URL: https://leetcode.com/problems/count-collisions-on-a-road/
# Difficulty: Medium
#
# Approach:
# Strip leading 'L' cars (they never collide with anything) and trailing 'R'
# cars (they drive off the end). Every remaining car that is not 'R' counts as
# a collision result, and every 'R' among the remaining cars also collides
# (it will eventually hit a stationary or leftward car).
# Equivalently: total collisions = len(stripped) - stripped.count('S')
# because each 'R' and each 'L' in the stripped string contributes exactly
# one collision and stops, becoming 'S'; all original 'S' contribute 0.
# Simpler: count non-'S' chars in the middle section, which equals
# len(stripped) - stripped.count('S').

class Solution(object):
    def countCollisions(self, directions):
        """
        :type directions: str
        :rtype: int
        """
        # Remove leading 'L' (go left off the left edge, no collision)
        # Remove trailing 'R' (go right off the right edge, no collision)
        stripped = directions.lstrip('L').rstrip('R')
        # Every non-'S' car in the remaining string will collide exactly once
        return len(stripped) - stripped.count('S')
