from typing import List
from functools import lru_cache

class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        n = len(coins)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        @lru_cache(maxsize=None)
        def dfs(node, par, halvings):
            c = coins[node] >> halvings
            children = [ch for ch in adj[node] if ch != par]
            opt1 = (c - k) + sum(dfs(ch, node, halvings) for ch in children)
            opt2 = (c >> 1) + sum(dfs(ch, node, halvings + 1) for ch in children)
            return max(opt1, opt2)

        return dfs(0, -1, 0)
