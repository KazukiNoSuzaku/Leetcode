# Author: Kaustav Ghosh
# https://leetcode.com/problems/destroying-asteroids/

class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        asteroids.sort()
        for a in asteroids:
            if mass >= a:
                mass += a
            else:
                return False
        return True
