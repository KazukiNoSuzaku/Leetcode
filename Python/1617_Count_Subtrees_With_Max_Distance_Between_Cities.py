# Author: Kaustav Ghosh
# Problem: Count Subtrees With Max Distance Between Cities
# Approach: There are at most fifteen cities, so every one of the 2^15 subsets of cities can be examined directly, and the only questions per subset are whether the cities it names hang together as one connected piece and, if so, how far apart its two most distant members are. All-pairs distances in the whole tree are computed once by Floyd-Warshall up front, so a subset's diameter is read off those precomputed numbers; connectivity is settled by counting the edges lying wholly inside the subset, since a subgraph of a tree on k vertices is connected exactly when it has k-1 edges. Each subset therefore costs only a scan over its own pairs.

class Solution(object):
    def countSubgraphsForEachDiameter(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        INF = float('inf')
        distance = [[INF] * n for _ in range(n)]
        for i in range(n):
            distance[i][i] = 0
        for a, b in edges:
            distance[a - 1][b - 1] = 1
            distance[b - 1][a - 1] = 1
        for k in range(n):
            dk = distance[k]
            for i in range(n):
                di = distance[i]
                through = di[k]
                if through == INF:
                    continue
                for j in range(n):
                    if through + dk[j] < di[j]:
                        di[j] = through + dk[j]

        pairs = [(a - 1, b - 1) for a, b in edges]
        counts = [0] * (n - 1)
        for mask in range(1, 1 << n):
            members = [i for i in range(n) if (mask >> i) & 1]
            if len(members) < 2:
                continue
            # A subgraph of a tree is connected exactly when it is a tree itself.
            inside = sum(1 for a, b in pairs if (mask >> a) & 1 and (mask >> b) & 1)
            if inside != len(members) - 1:
                continue
            diameter = 0
            for x in range(len(members)):
                row = distance[members[x]]
                for y in range(x + 1, len(members)):
                    if row[members[y]] > diameter:
                        diameter = row[members[y]]
            counts[diameter - 1] += 1
        return counts
