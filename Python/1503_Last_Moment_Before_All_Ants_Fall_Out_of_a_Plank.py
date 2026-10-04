# Author: Kaustav Ghosh
# Problem: Last Moment Before All Ants Fall Out of a Plank
# Approach: Two ants bouncing off each other is indistinguishable from the two passing straight through and swapping identities, since they are identical. So every ant simply walks its own way off the plank, and the last moment is the longest single journey: the furthest left-mover's position, or the furthest right-mover's distance to the end

class Solution(object):
    def getLastMoment(self, n, left, right):
        """
        :type n: int
        :type left: List[int]
        :type right: List[int]
        :rtype: int
        """
        return max(max(left, default=0), n - min(right, default=n))
