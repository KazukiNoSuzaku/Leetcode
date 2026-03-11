# Find the quietest person at least as rich as each person.

# Author: Kaustav Ghosh

from collections import defaultdict

class Solution(object):
    def loudAndRich(self, richer, quiet):
        n = len(quiet)
        graph = defaultdict(list)
        for a, b in richer: graph[b].append(a)
        res = [-1] * n
        def dfs(node):
            if res[node] != -1: return res[node]
            res[node] = node
            for richer_node in graph[node]:
                cand = dfs(richer_node)
                if quiet[cand] < quiet[res[node]]:
                    res[node] = cand
            return res[node]
        for i in range(n): dfs(i)
        return res
