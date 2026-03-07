# You are given an empty 2D binary grid grid of size m x n. The grid represents a map where
# 0's represent water and 1's represent land. Initially, all the cells of grid are water cells.
# We may perform an addLand operation which turns the water at position (r, c) into land.
# Given a list of positions to operate, count the number of islands after each addLand operation.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

# Example 1:
# Input: m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
# Output: [1,1,2,3]

# Constraints:
# 1 <= m, n <= 10^4
# 1 <= positions.length <= 10^4

# Author: Kaustav Ghosh

class Solution(object):
    def numIslands2(self, m, n, positions):
        parent = {}
        rank = {}
        count = [0]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank.get(ra, 0) < rank.get(rb, 0):
                ra, rb = rb, ra
            parent[rb] = ra
            rank[ra] = rank.get(ra, 0) + (1 if rank.get(ra, 0) == rank.get(rb, 0) else 0)
            count[0] -= 1

        res = []
        for r, c in positions:
            if (r, c) in parent:
                res.append(count[0])
                continue
            parent[(r, c)] = (r, c)
            count[0] += 1
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nb = (r + dr, c + dc)
                if nb in parent:
                    union((r, c), nb)
            res.append(count[0])
        return res
