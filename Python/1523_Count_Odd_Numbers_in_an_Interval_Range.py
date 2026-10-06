# Author: Kaustav Ghosh
# Problem: Count Odd Numbers in an Interval Range
# Approach: There are (n + 1) / 2 odd numbers in 1..n, so subtracting the count below low from the count up to high gives the answer without looping

class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        return (high + 1) // 2 - low // 2
