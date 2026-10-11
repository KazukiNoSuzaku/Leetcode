# Author: Kaustav Ghosh
# Problem: Minimum Time to Make Rope Colorful
# Approach: Only runs of the same colour are a problem, and runs are independent of one another, so within each maximal run of identical colours exactly one balloon must survive and it should be the most expensive one to remove; the cost of that run is therefore its total time minus its largest time. One pass is enough: I accumulate the running total and running maximum while the colour stays the same, and bank total minus maximum whenever the colour changes.

class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        spent = 0
        run_total = run_max = 0
        previous = ''
        for colour, time in zip(colors, neededTime):
            if colour != previous:
                spent += run_total - run_max
                run_total = run_max = 0
                previous = colour
            run_total += time
            if time > run_max:
                run_max = time
        return spent + run_total - run_max
