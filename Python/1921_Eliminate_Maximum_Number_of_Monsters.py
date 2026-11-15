# Author: Kaustav Ghosh
# Problem: Eliminate Maximum Number of Monsters
# Approach: Shooting the monster that would arrive soonest is always at least as good as any other choice, so the monsters are sorted by arrival and taken in that order; the run ends at the first one that reaches the city before its turn comes round. The arrival times are kept as whole minutes rather than fractions: a monster can still be shot during minutes zero up to its arrival time rounded up minus one, so rounding up the division captures exactly the number of chances there are to kill it. That keeps both the sort and the comparison in integers, with no floating-point ratio to tip a close ordering the wrong way.

class Solution(object):
    def eliminateMaximum(self, dist, speed):
        """
        :type dist: List[int]
        :type speed: List[int]
        :rtype: int
        """
        arrivals = sorted(-(-d // s) for d, s in zip(dist, speed))
        for minute, arrival in enumerate(arrivals):
            if arrival <= minute:
                return minute
        return len(arrivals)
