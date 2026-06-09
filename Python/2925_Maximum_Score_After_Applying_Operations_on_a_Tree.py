from typing import List

class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        n = len(values)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node, par):
            children = [c for c in adj[node] if c != par]
            if not children:
                return values[node]
            child_cost = sum(dfs(c, node) for c in children)
            # min cost to cover all root-to-leaf paths through this node
            return min(values[node], child_cost)

        total = sum(values)
        sacrifice = sum(dfs(c, 0) for c in adj[0])
        return total - sacrifice
