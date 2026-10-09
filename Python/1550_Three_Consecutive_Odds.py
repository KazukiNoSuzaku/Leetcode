# Author: Kaustav Ghosh
# Problem: Three Consecutive Odds
# Approach: Count consecutive odd values, resetting on anything even, and report success as soon as the run reaches three

class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        run = 0
        for x in arr:
            run = run + 1 if x % 2 else 0
            if run == 3:
                return True
        return False
