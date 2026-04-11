# Author: Kaustav Ghosh
# Problem: 2285. Maximum Total Importance of Roads
# URL: https://leetcode.com/problems/maximum-total-importance-of-roads/
# Difficulty: Medium
#
# Approach:
# Count degree of each node. Assign highest values to nodes with highest degree.
# Total importance = sum of degree[i] * assigned_value[i].

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
        total = 0
        for i in range(n):
            total += degree[i] * (i + 1)
        return total
