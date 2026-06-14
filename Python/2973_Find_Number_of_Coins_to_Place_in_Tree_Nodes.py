from typing import List
from collections import defaultdict

class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        n = len(cost)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        ans = [1] * n

        def dfs(node: int, parent: int) -> list:
            vals = [cost[node]]
            for child in graph[node]:
                if child != parent:
                    vals.extend(dfs(child, node))
            if len(vals) >= 3:
                vals.sort()
                ans[node] = max(0, max(vals[-1] * vals[-2] * vals[-3],
                                       vals[0] * vals[1] * vals[-1]))
            elif len(vals) < 3:
                ans[node] = 1
            return vals if len(vals) <= 6 else vals[-3:] + vals[:3]

        dfs(0, -1)
        return ans
