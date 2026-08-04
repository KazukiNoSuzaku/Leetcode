# Author: Kaustav Ghosh
# Problem: Eliminate Maximum Number of Monsters
# Approach: A monster's arrival time is dist/speed. Sort arrivals ascending; you fire once per minute, so at minute i you can kill the i-th soonest monster only if it has not already arrived (arrival > i). The first monster with arrival <= its index ends the game

class Solution(object):
    def eliminateMaximum(self, dist, speed):
        """
        :type dist: List[int]
        :type speed: List[int]
        :rtype: int
        """
        arrivals = sorted(d / float(s) for d, s in zip(dist, speed))
        for i, t in enumerate(arrivals):
            if t <= i:
                return i
        return len(arrivals)
