# Author: Kaustav Ghosh
# Problem: Count Collisions on a Road
# Approach: Cars that escape off the ends (leading 'L's and trailing 'R's) never collide, so strip them. Within what remains, every moving car ('L' or 'R') is guaranteed to eventually hit something and stop, contributing exactly one collision, so the answer is the number of non-'S' cars in the trimmed string

class Solution(object):
    def countCollisions(self, directions):
        """
        :type directions: str
        :rtype: int
        """
        s = directions.lstrip('L').rstrip('R')
        # In the trimmed section, every car that is still moving eventually
        # collides and stops; count all cars that are not stationary 'S'.
        return sum(1 for c in s if c != 'S')
