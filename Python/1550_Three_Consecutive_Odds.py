# Author: Kaustav Ghosh
# Problem: Three Consecutive Odds
# Approach: Single pass counting consecutive odd numbers; reset on any even, return True once the streak hits three

class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = 0
        for x in arr:
            if x % 2 == 1:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0
        return False
