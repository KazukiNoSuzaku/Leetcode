# Author: Kaustav Ghosh
# Problem: Valid Arrangement of Pairs
# Approach: The pairs form a directed multigraph; a valid arrangement is an Eulerian path. Pick the start node (out-degree exceeds in-degree by one, else any node) and run Hierholzer's algorithm, then read consecutive nodes as the ordered pairs

from collections import defaultdict

class Solution(object):
    def validArrangement(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: List[List[int]]
        """
        graph = defaultdict(list)
        out_deg = defaultdict(int)
        in_deg = defaultdict(int)
        for a, b in pairs:
            graph[a].append(b)
            out_deg[a] += 1
            in_deg[b] += 1

        start = pairs[0][0]
        for node in out_deg:
            if out_deg[node] - in_deg[node] == 1:
                start = node
                break

        # Hierholzer's algorithm (iterative)
        stack = [start]
        route = []
        while stack:
            u = stack[-1]
            if graph[u]:
                stack.append(graph[u].pop())
            else:
                route.append(stack.pop())
        route.reverse()

        return [[route[i], route[i + 1]] for i in range(len(route) - 1)]
