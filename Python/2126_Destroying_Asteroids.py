# Author: Kaustav Ghosh
# Problem: Destroying Asteroids
# Approach: Sort asteroids ascending and absorb them in order. Each must be no heavier than the current mass; absorbing adds its mass. If any is too heavy, the planet cannot destroy them all

class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        for a in sorted(asteroids):
            if a > mass:
                return False
            mass += a
        return True
