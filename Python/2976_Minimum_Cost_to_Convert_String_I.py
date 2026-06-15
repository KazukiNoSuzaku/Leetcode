from typing import List

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str],
                    changed: List[str], cost: List[int]) -> int:
        INF = float('inf')
        dist = [[INF] * 26 for _ in range(26)]
        for i in range(26):
            dist[i][i] = 0
        for a, b, c in zip(original, changed, cost):
            u, v = ord(a) - 97, ord(b) - 97
            dist[u][v] = min(dist[u][v], c)
        for k in range(26):
            for i in range(26):
                if dist[i][k] == INF:
                    continue
                for j in range(26):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        total = 0
        for s, t in zip(source, target):
            u, v = ord(s) - 97, ord(t) - 97
            if dist[u][v] == INF:
                return -1
            total += dist[u][v]
        return total
