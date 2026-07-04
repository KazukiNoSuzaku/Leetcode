# Author: Kaustav Ghosh
# Problem: Count Subtrees With Max Distance Between Cities
# Approach: n<=15, so enumerate every node subset; in a tree a subset is a connected subtree iff its internal edges == nodes-1, then its diameter (max pairwise Floyd-Warshall distance) buckets the answer

class Solution(object):
    def countSubgraphsForEachDiameter(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        INF = float('inf')
        dist = [[INF] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for a, b in edges:
            a, b = a - 1, b - 1
            dist[a][b] = dist[b][a] = 1
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        ans = [0] * (n - 1)
        for mask in range(1, 1 << n):
            nodes = [i for i in range(n) if mask >> i & 1]
            if len(nodes) < 2:
                continue
            internal = sum(1 for a, b in edges
                           if mask >> (a - 1) & 1 and mask >> (b - 1) & 1)
            if internal != len(nodes) - 1:
                continue  # not a connected subtree
            diameter = max(dist[i][j] for i in nodes for j in nodes)
            ans[diameter - 1] += 1
        return ans
