# Author: Kaustav Ghosh
# https://leetcode.com/problems/maximal-network-rank/

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
            connected.add((min(a, b), max(a, b)))

        max_rank = 0
        for i in range(n):
            for j in range(i + 1, n):
                rank = degree[i] + degree[j]
                if (i, j) in connected:
                    rank -= 1
                max_rank = max(max_rank, rank)
        return max_rank
