# Given an n-ary tree, return the level order traversal of its nodes' values.

# Author: Kaustav Ghosh

from collections import deque

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        res = []
        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                queue.extend(node.children)
            res.append(level)
        return res
