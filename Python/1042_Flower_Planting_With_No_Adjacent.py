# Author: Kaustav Ghosh
# 1042. Flower Planting With No Adjacent
# https://leetcode.com/problems/flower-planting-with-no-adjacent/

class Solution(object):
    def gardenNoAdj(self, n, paths):
        """
        :type n: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in range(n + 1)]
        for u, v in paths:
            graph[u].append(v)
            graph[v].append(u)
        result = [0] * (n + 1)
        for garden in range(1, n + 1):
            used = {result[nb] for nb in graph[garden]}
            for color in range(1, 5):
                if color not in used:
                    result[garden] = color
                    break
        return result[1:]
