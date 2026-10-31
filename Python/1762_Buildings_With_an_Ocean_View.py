# Author: Kaustav Ghosh
# Problem: Buildings With an Ocean View
# Approach: A building sees the ocean exactly when every building to its right is strictly shorter, which only depends on the tallest building to the right. Walking the array from right to left keeps that running maximum available for free, so each index is kept when its height beats everything seen so far and the maximum is then raised to it. The indices come out in decreasing order, so the list is reversed at the end; one pass and no stack.

class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        visible = []
        tallest_to_right = 0
        for index in range(len(heights) - 1, -1, -1):
            if heights[index] > tallest_to_right:
                visible.append(index)
                tallest_to_right = heights[index]
        visible.reverse()
        return visible
