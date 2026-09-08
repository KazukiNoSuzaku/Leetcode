# Author: Kaustav Ghosh
# Problem: Maximum Total Importance of Roads
# Approach: Each road contributes the sum of its two cities' assigned values, so a city's total contribution is its degree times its value. To maximize, give the largest values to the highest-degree cities: sort degrees ascending and pair them with values 1..n

class Solution(object):
    def maximumImportance(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        degree = [0] * n
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
        degree.sort()
        return sum(d * (i + 1) for i, d in enumerate(degree))
