# Author: Kaustav Ghosh
# Problem: Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
# Approach: Kruskal variants: exclude each edge (critical if MST weight increases),
#           force-include each edge (pseudo-critical if MST weight stays same)

class Solution(object):
    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :type n: int
        :rtype: List[List[int]]
        """
        indexed_edges = [(w, u, v, i) for i, (u, v, w) in enumerate(edges)]
        indexed_edges.sort()

        def find(parent, x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def kruskal(n, edges, include=-1, exclude=-1):
            parent = list(range(n))
            rank = [0] * n
            weight = 0
            count = 0

            def union(a, b):
                ra, rb = find(parent, a), find(parent, b)
                if ra == rb:
                    return False
                if rank[ra] < rank[rb]:
                    ra, rb = rb, ra
                parent[rb] = ra
                if rank[ra] == rank[rb]:
                    rank[ra] += 1
                return True

            if include != -1:
                w, u, v, _ = indexed_edges[include]
                if union(u, v):
                    weight += w
                    count += 1

            for idx, (w, u, v, i) in enumerate(indexed_edges):
                if idx == exclude:
                    continue
                if union(u, v):
                    weight += w
                    count += 1
            return weight if count == n - 1 else float('inf')

        mst_weight = kruskal(n, indexed_edges)
        critical = []
        pseudo_critical = []

        for idx in range(len(indexed_edges)):
            # Check critical
            if kruskal(n, indexed_edges, exclude=idx) > mst_weight:
                critical.append(indexed_edges[idx][3])
            # Check pseudo-critical
            elif kruskal(n, indexed_edges, include=idx) == mst_weight:
                pseudo_critical.append(indexed_edges[idx][3])

        return [critical, pseudo_critical]
