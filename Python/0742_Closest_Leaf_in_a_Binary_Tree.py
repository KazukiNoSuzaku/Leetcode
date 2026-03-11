# Find the closest leaf to node k in a binary tree.

# Author: Kaustav Ghosh

from collections import defaultdict, deque

class Solution(object):
    def findClosestLeaf(self, root, k):
        graph = defaultdict(list)
        def dfs(node, parent):
            if not node: return
            if parent: graph[node].append(parent); graph[parent].append(node)
            dfs(node.left, node)
            dfs(node.right, node)
        dfs(root, None)
        q = deque()
        for node in graph:
            if node.val == k: q.append(node); break
        visited = set(q)
        while q:
            node = q.popleft()
            if not node.left and not node.right: return node.val
            for nb in graph[node]:
                if nb not in visited:
                    visited.add(nb)
                    q.append(nb)
        return -1
