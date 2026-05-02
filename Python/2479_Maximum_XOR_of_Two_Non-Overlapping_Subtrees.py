from collections import defaultdict

class Solution:
    def maxXor(self, n: int, edges: list[list[int]], values: list[int]) -> int:
        # Premium: find two subtrees with no shared nodes that maximize XOR of their sums.
        # Two subtrees are non-overlapping iff neither root is an ancestor of the other.
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        subtree_sum = list(values)
        in_time = [0] * n
        out_time = [0] * n
        timer = [0]

        def dfs(node, parent):
            in_time[node] = timer[0]
            timer[0] += 1
            for nei in adj[node]:
                if nei != parent:
                    dfs(nei, node)
                    subtree_sum[node] += subtree_sum[nei]
            out_time[node] = timer[0]
            timer[0] += 1

        dfs(0, -1)

        def is_ancestor(u, v):
            return in_time[u] <= in_time[v] <= out_time[v] <= out_time[u]

        ans = 0
        for u in range(n):
            for v in range(u + 1, n):
                if not is_ancestor(u, v) and not is_ancestor(v, u):
                    ans = max(ans, subtree_sum[u] ^ subtree_sum[v])
        return ans
