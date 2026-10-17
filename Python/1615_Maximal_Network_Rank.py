# Author: Kaustav Ghosh
# Problem: Maximal Network Rank
# Approach: The rank of a pair is the sum of the two cities' road counts, except that a road running directly between them is shared and so would be counted twice, which means the only thing needed beyond the degrees is the ability to ask whether a given pair is joined. I count degrees in one pass and keep the roads in a set of ordered pairs, then with at most a hundred cities simply evaluate every pair, which is a few thousand constant-time checks.

class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        degree = [0] * n
        linked = set()
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
            linked.add((a, b) if a < b else (b, a))

        best = 0
        for i in range(n):
            for j in range(i + 1, n):
                rank = degree[i] + degree[j]
                if (i, j) in linked:
                    rank -= 1
                if rank > best:
                    best = rank
        return best
