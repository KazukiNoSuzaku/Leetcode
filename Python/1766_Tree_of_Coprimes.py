# Author: Kaustav Ghosh

class Solution(object):
    def getCoprimes(self, nums, edges):
        """
        :type nums: List[int]
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        from math import gcd
        from collections import defaultdict
        n = len(nums)
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        # Precompute coprime pairs for values 1..50
        coprimes = defaultdict(list)
        for i in range(1, 51):
            for j in range(1, 51):
                if gcd(i, j) == 1:
                    coprimes[i].append(j)
        ans = [-1] * n
        # For each value, maintain stack of (node, depth)
        val_stack = defaultdict(list)
        visited = [False] * n

        def dfs(node, depth):
            visited[node] = True
            best_depth = -1
            best_ancestor = -1
            for v in coprimes[nums[node]]:
                if val_stack[v]:
                    anc, d = val_stack[v][-1]
                    if d > best_depth:
                        best_depth = d
                        best_ancestor = anc
            ans[node] = best_ancestor
            val_stack[nums[node]].append((node, depth))
            for child in adj[node]:
                if not visited[child]:
                    dfs(child, depth + 1)
            val_stack[nums[node]].pop()

        import sys
        sys.setrecursionlimit(200000)
        dfs(0, 0)
        return ans
