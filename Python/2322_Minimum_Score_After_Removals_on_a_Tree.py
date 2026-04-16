# Author: Kaustav Ghosh
# Problem: 2322. Minimum Score After Removals on a Tree
# URL: https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/
# Difficulty: Hard
# Note: Premium problem
#
# Approach:
# Root the tree and compute XOR of each subtree. For each pair of edges (e1, e2) removed,
# the three components' XOR values can be determined. If one subtree is ancestor of the other,
# the three values are: subtree(deeper), subtree(shallower) XOR subtree(deeper), total XOR subtree(shallower).
# Otherwise: subtree(e1), subtree(e2), total XOR subtree(e1) XOR subtree(e2).
# Minimize max - min over all valid edge pairs.

# SQL (N/A - this is a Python/tree problem)

class Solution(object):
    def minimumScore(self, nums, edges):
        """
        :type nums: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict

        n = len(nums)
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        subtree_xor = nums[:]
        order = []
        parent = [-1] * n
        depth = [0] * n
        visited = [False] * n

        # BFS to get order
        from collections import deque
        queue = deque([0])
        visited[0] = True
        while queue:
            node = queue.popleft()
            order.append(node)
            for nb in adj[node]:
                if not visited[nb]:
                    visited[nb] = True
                    parent[nb] = node
                    depth[nb] = depth[node] + 1
                    queue.append(nb)

        # Compute subtree XOR in reverse BFS order
        for node in reversed(order):
            if parent[node] != -1:
                subtree_xor[parent[node]] ^= subtree_xor[node]

        total = subtree_xor[0]

        # Check if u is ancestor of v
        # Use entry/exit times
        tin = [0] * n
        tout = [0] * n
        timer = [0]

        def dfs(u, p):
            tin[u] = timer[0]
            timer[0] += 1
            for v in adj[u]:
                if v != p:
                    dfs(v, u)
            tout[u] = timer[0]
            timer[0] += 1

        import sys
        sys.setrecursionlimit(100000)
        dfs(0, -1)

        def is_ancestor(u, v):
            return tin[u] <= tin[v] and tout[v] <= tout[u]

        ans = float('inf')
        # Enumerate all pairs of non-root nodes (each edge i represented by its child node)
        nodes = order[1:]  # exclude root
        m = len(nodes)
        for i in range(m):
            for j in range(i + 1, m):
                u, v = nodes[i], nodes[j]
                xu, xv = subtree_xor[u], subtree_xor[v]
                if is_ancestor(u, v):
                    # v is in subtree of u
                    a, b, c = xv, xu ^ xv, total ^ xu
                elif is_ancestor(v, u):
                    # u is in subtree of v
                    a, b, c = xu, xv ^ xu, total ^ xv
                else:
                    a, b, c = xu, xv, total ^ xu ^ xv
                ans = min(ans, max(a, b, c) - min(a, b, c))

        return ans
