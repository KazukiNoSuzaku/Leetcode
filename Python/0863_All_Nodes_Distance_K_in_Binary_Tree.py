# Find all nodes at distance k from a target node in a binary tree.

# Author: Kaustav Ghosh

from collections import defaultdict, deque

class Solution(object):
    def distanceK(self, root, target, k):
        graph = defaultdict(list)
        def build(node, parent):
            if not node: return
            if parent: graph[node.val].append(parent.val); graph[parent.val].append(node.val)
            build(node.left, node)
            build(node.right, node)
        build(root, None)
        q = deque([(target.val, 0)])
        visited = {target.val}
        res = []
        while q:
            node, dist = q.popleft()
            if dist == k: res.append(node)
            for nb in graph[node]:
                if nb not in visited:
                    visited.add(nb)
                    q.append((nb, dist + 1))
        return res
