# Author: Kaustav Ghosh
# Problem: Tree of Coprimes
# Approach: Values are small (<=50), so keep a stack of ancestors per value during an iterative DFS. For each node pick the deepest coprime-value ancestor across those stacks; enter/exit events keep the stacks in sync

from math import gcd

class Solution(object):
    def getCoprimes(self, nums, edges):
        """
        :type nums: List[int]
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        coprime = [[u for u in range(1, 51) if gcd(v, u) == 1] for v in range(51)]
        ans = [-1] * n
        stacks = [[] for _ in range(51)]  # value -> list of (node, depth)

        # Iterative DFS with explicit enter/exit events
        stack = [(0, -1, 0, False)]
        while stack:
            node, parent, depth, exiting = stack.pop()
            if exiting:
                stacks[nums[node]].pop()
                continue

            best_depth, best_node = -1, -1
            for u in coprime[nums[node]]:
                if stacks[u] and stacks[u][-1][1] > best_depth:
                    best_node, best_depth = stacks[u][-1][0], stacks[u][-1][1]
            ans[node] = best_node

            stacks[nums[node]].append((node, depth))
            stack.append((node, parent, depth, True))
            for nb in adj[node]:
                if nb != parent:
                    stack.append((nb, node, depth + 1, False))

        return ans
