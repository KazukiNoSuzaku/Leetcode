from typing import List

class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        INF = float('inf')
        dist = [[INF] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for u, v, w in roads:
            dist[u][v] = min(dist[u][v], w)
            dist[v][u] = min(dist[v][u], w)
        for k in range(n):
            for i in range(n):
                if dist[i][k] == INF:
                    continue
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        # bad[i] = bitmask of nodes incompatible with node i
        bad = [0] * n
        for i in range(n):
            for j in range(n):
                if i != j and dist[i][j] > maxDistance:
                    bad[i] |= 1 << j

        # valid[mask] via DP: adding lowest set bit must not conflict with rest
        valid = [True] * (1 << n)
        for mask in range(1, 1 << n):
            lsb = mask & -mask
            lsb_pos = lsb.bit_length() - 1
            rest = mask ^ lsb
            valid[mask] = valid[rest] and (bad[lsb_pos] & rest) == 0

        return sum(valid)
