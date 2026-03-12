# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Kruskal's MST with Union-Find

class Solution(object):
    def minimumCost(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        parent = list(range(n + 1))
        rank = [0] * (n + 1)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
            return True

        connections.sort(key=lambda x: x[2])
        total = 0
        edges = 0
        for u, v, w in connections:
            if union(u, v):
                total += w
                edges += 1
                if edges == n - 1:
                    return total
        return -1 if edges < n - 1 else total
