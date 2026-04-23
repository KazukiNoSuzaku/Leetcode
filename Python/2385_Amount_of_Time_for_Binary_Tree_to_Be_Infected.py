from collections import defaultdict, deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)

        def build(node, parent):
            if not node:
                return
            if parent is not None:
                graph[node.val].append(parent)
                graph[parent].append(node.val)
            build(node.left, node.val)
            build(node.right, node.val)

        build(root, None)
        visited = {start}
        q = deque([start])
        minutes = -1
        while q:
            minutes += 1
            for _ in range(len(q)):
                node = q.popleft()
                for nb in graph[node]:
                    if nb not in visited:
                        visited.add(nb)
                        q.append(nb)
        return minutes
