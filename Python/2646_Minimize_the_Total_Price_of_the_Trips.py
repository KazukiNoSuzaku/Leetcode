from collections import defaultdict

class Solution:
    def minimumTotalPrice(self, n: int, edges: list[list[int]], price: list[int], trips: list[list[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        count = [0] * n

        def find_path(src, dst, parent):
            if src == dst:
                count[src] += 1
                return True
            for nb in adj[src]:
                if nb != parent and find_path(nb, src, src):
                    count[src] += 1
                    return True
            return False

        for s, e in trips:
            find_path(s, e, -1)

        def dfs(node, parent):
            # Returns (cost_not_halved, cost_halved) for this subtree
            full = price[node] * count[node]
            half = price[node] // 2 * count[node]
            not_h, h = full, half
            for nb in adj[node]:
                if nb != parent:
                    child_not_h, child_h = dfs(nb, node)
                    not_h += min(child_not_h, child_h)
                    h += child_not_h
            return not_h, h

        return min(dfs(0, -1))
