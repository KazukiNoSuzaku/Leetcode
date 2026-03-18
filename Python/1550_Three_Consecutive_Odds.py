# Author: Kaustav Ghosh
# Problem: 1550 - Three Consecutive Odds
# Approach: Scan for 3 consecutive odd numbers

class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = 0
        for num in arr:
            if num % 2 == 1:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0
        return False
