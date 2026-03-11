# There are n cities, some of which are connected, forming a province.
# Given an n x n matrix isConnected, return the total number of provinces.

# Author: Kaustav Ghosh

class Solution(object):
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        parent = list(range(n))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x, y):
            parent[find(x)] = find(y)
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j]:
                    union(i, j)
        return sum(1 for i in range(n) if find(i) == i)
