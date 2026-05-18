from collections import deque

class Solution:
    def collectTheCoins(self, coins: list[int], edges: list[list[int]]) -> int:
        n = len(coins)
        graph = [set() for _ in range(n)]
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        # Step 1: remove all 0-value leaves repeatedly
        q = deque(i for i in range(n) if len(graph[i]) == 1 and coins[i] == 0)
        while q:
            node = q.popleft()
            for nb in list(graph[node]):
                graph[nb].discard(node)
                if len(graph[nb]) == 1 and coins[nb] == 0:
                    q.append(nb)
            graph[node].clear()

        # Step 2: remove 2 more layers of leaves (coins reachable from parent/grandparent)
        for _ in range(2):
            leaves = [i for i in range(n) if len(graph[i]) == 1]
            for node in leaves:
                for nb in list(graph[node]):
                    graph[nb].discard(node)
                graph[node].clear()

        # Each remaining edge must be traversed twice
        return sum(len(g) for g in graph)  # sum of degrees = 2 * edge_count
