# Author: Kaustav Ghosh
# Problem: Count Odd Numbers in an Interval Range
# Approach: Odd count up to n = (n+1)//2; answer = odds up to high minus odds up to low-1

class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        return (high + 1) // 2 - low // 2
