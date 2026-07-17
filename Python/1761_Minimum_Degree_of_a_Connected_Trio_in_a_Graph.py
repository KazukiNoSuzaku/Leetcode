# Author: Kaustav Ghosh
# Problem: Minimum Degree of a Connected Trio in a Graph
# Approach: For every edge (u,v) find a common neighbor w to complete a trio; its outward degree is deg[u]+deg[v]+deg[w] minus the 6 internal edge-endpoints

class Solution(object):
    def minTrioDegree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        connected = [[False] * (n + 1) for _ in range(n + 1)]
        degree = [0] * (n + 1)
        for u, v in edges:
            connected[u][v] = connected[v][u] = True
            degree[u] += 1
            degree[v] += 1

        best = float('inf')
        for u, v in edges:
            for w in range(1, n + 1):
                if connected[u][w] and connected[v][w]:
                    best = min(best, degree[u] + degree[v] + degree[w] - 6)

        return best if best != float('inf') else -1
