# Author: Kaustav Ghosh
# Problem: Maximum Consecutive Floors Without Special Floors
# Approach: Sort the special floors and measure the runs of ordinary floors between consecutive specials, plus the run below the first special and above the last. The largest such run is the answer

class Solution(object):
    def maxConsecutive(self, bottom, top, special):
        """
        :type bottom: int
        :type top: int
        :type special: List[int]
        :rtype: int
        """
        special.sort()
        best = max(special[0] - bottom, top - special[-1])
        for i in range(1, len(special)):
            best = max(best, special[i] - special[i - 1] - 1)
        return best
