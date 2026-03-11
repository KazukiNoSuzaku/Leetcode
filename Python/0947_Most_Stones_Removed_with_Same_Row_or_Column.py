# Remove max stones where each stone shares row or column with another.

# Author: Kaustav Ghosh

class Solution(object):
    def removeStones(self, stones):
        parent = {}
        def find(x):
            parent.setdefault(x, x)
            if parent[x] != x: parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            parent[find(x)] = find(y)
        for r, c in stones:
            union(r, ~c)
        return len(stones) - len({find(r) for r, c in stones})
