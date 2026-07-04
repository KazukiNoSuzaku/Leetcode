# Author: Kaustav Ghosh
# Problem: Maximal Network Rank
# Approach: Rank of a pair is the sum of their degrees minus one if a road directly connects them; try every pair

class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        degree = [0] * n
        connected = set()
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
            connected.add((a, b))
            connected.add((b, a))

        best = 0
        for i in range(n):
            for j in range(i + 1, n):
                rank = degree[i] + degree[j] - (1 if (i, j) in connected else 0)
                best = max(best, rank)
        return best
