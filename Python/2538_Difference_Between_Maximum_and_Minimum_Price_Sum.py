from collections import defaultdict

class Solution:
    def maxOutput(self, n: int, edges: list[list[int]], price: list[int]) -> int:
        # Tree DFS returning (inc, exc): max path sum rooted here with/without counting this node's price.
        # Answer = max over all nodes of (inc from child A + exc from child B), avoiding double-counting root.
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        ans = 0

        def dfs(node, parent):
            nonlocal ans
            inc = price[node]  # best arm including this node
            exc = 0            # best arm excluding this node (i.e. arm ends at a descendant)
            for child in adj[node]:
                if child == parent:
                    continue
                c_inc, c_exc = dfs(child, node)
                # candidate answer: best arm from one child (inc) + best arm from another (exc of this node so far)
                ans = max(ans, c_inc + exc, c_exc + inc)
                inc = max(inc, c_inc + price[node])
                exc = max(exc, c_exc, c_inc)
            return inc, exc

        dfs(0, -1)
        return ans
