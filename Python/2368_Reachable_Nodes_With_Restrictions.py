# Author: Kaustav Ghosh
# Problem: Reachable Nodes With Restrictions
# Approach: Build the adjacency lists, then walk the tree from node 0 with a stack, never stepping onto a restricted node. In a tree that single traversal reaches exactly the nodes whose path from 0 avoids every restricted node

from collections import defaultdict


class Solution(object):
    def reachableNodes(self, n, edges, restricted):
        """
        :type n: int
        :type edges: List[List[int]]
        :type restricted: List[int]
        :rtype: int
        """
        blocked = set(restricted)
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        seen = {0}
        stack = [0]
        while stack:
            node = stack.pop()
            for nxt in graph[node]:
                if nxt not in seen and nxt not in blocked:
                    seen.add(nxt)
                    stack.append(nxt)
        return len(seen)
