# Find the city with the fewest reachable cities within distanceThreshold.
# Return the city with the largest index if tie.

# Author: Kaustav Ghosh

class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        INF = float('inf')
        dist = [[INF] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for u, v, w in edges:
            dist[u][v] = dist[v][u] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        res, min_count = 0, n
        for i in range(n):
            count = sum(1 for j in range(n) if i != j and dist[i][j] <= distanceThreshold)
            if count <= min_count:
                min_count = count
                res = i
        return res
