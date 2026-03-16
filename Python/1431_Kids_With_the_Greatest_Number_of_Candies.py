# Author: Kaustav Ghosh
# Problem: Kids With the Greatest Number of Candies
# Approach: Check if candies[i] + extraCandies >= max(candies)

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candies = max(candies)
        return [c + extraCandies >= max_candies for c in candies]
