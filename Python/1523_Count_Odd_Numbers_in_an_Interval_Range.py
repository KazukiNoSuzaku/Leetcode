# Author: Kaustav Ghosh
# Problem: 1523 - Count Odd Numbers in an Interval Range
# Approach: (high+1)//2 - low//2

class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        return (high + 1) // 2 - low // 2
