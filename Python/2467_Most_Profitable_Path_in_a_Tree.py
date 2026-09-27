# Author: Kaustav Ghosh
# Problem: Most Profitable Path in a Tree
# Approach: Bob's route is forced, the unique path from his node up to the root, so record the minute he reaches each node on it. Alice then explores every root-to-leaf path with a stack, carrying the minute and her income: a gate Bob reached earlier is already spent, one they reach together is split, and any other gate is hers in full. The best income over all leaves wins

from collections import deque


class Solution(object):
    def mostProfitablePath(self, edges, bob, amount):
        """
        :type edges: List[List[int]]
        :type bob: int
        :type amount: List[int]
        :rtype: int
        """
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        parent = [-1] * n
        seen = [False] * n
        seen[0] = True
        queue = deque([0])
        while queue:
            node = queue.popleft()
            for nxt in graph[node]:
                if not seen[nxt]:
                    seen[nxt] = True
                    parent[nxt] = node
                    queue.append(nxt)

        bob_minute = {}
        minute = 0
        node = bob
        while node != -1:
            bob_minute[node] = minute
            minute += 1
            node = parent[node]

        best = float('-inf')
        stack = [(0, 0, 0)]
        while stack:
            node, time, income = stack.pop()
            gate = amount[node]
            if node in bob_minute:
                if time > bob_minute[node]:
                    gate = 0
                elif time == bob_minute[node]:
                    gate //= 2
            income += gate
            children = [child for child in graph[node] if child != parent[node]]
            if not children:
                best = max(best, income)
            for child in children:
                stack.append((child, time + 1, income))
        return best
