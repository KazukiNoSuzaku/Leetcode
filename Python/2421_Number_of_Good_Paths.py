# Author: Kaustav Ghosh
# Problem: Number of Good Paths
# Approach: A good path's endpoints share a value that no node on the way exceeds, so add the edges in increasing order of their larger endpoint value. When two components merge at value w, every node already holding w on one side pairs with every such node on the other, so add that product and carry forward how many nodes hold the component's maximum

class Solution(object):
    def numberOfGoodPaths(self, vals, edges):
        """
        :type vals: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        n = len(vals)
        parent = list(range(n))
        top = vals[:]
        at_top = [1] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        total = n
        for a, b in sorted(edges, key=lambda e: max(vals[e[0]], vals[e[1]])):
            ra, rb = find(a), find(b)
            if ra == rb:
                continue
            weight = max(vals[a], vals[b])
            if top[ra] == top[rb] == weight:
                total += at_top[ra] * at_top[rb]
                merged = at_top[ra] + at_top[rb]
            else:
                merged = at_top[ra] if top[ra] == weight else at_top[rb]
            parent[rb] = ra
            top[ra] = weight
            at_top[ra] = merged
        return total
