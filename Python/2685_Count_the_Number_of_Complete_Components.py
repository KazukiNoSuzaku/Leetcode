from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            parent[find(x)] = find(y)

        for u, v in edges:
            union(u, v)

        node_count = defaultdict(int)
        edge_count = defaultdict(int)
        for i in range(n):
            node_count[find(i)] += 1
        for u, v in edges:
            edge_count[find(u)] += 1

        return sum(
            1 for root, nc in node_count.items()
            if edge_count[root] == nc * (nc - 1) // 2
        )
