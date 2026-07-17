# Author: Kaustav Ghosh
# Problem: Buildings With an Ocean View (Premium)
# Approach: Scan from the right tracking the tallest seen so far; a building has a view when it exceeds everything to its right

class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        res = []
        tallest = 0
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > tallest:
                res.append(i)
                tallest = heights[i]
        return res[::-1]
