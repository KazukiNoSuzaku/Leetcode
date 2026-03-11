# Add a row of nodes with value val at depth d in a binary tree.

# Author: Kaustav Ghosh

from collections import deque

class Solution(object):
    def addOneRow(self, root, val, depth):
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        q = deque([root])
        for _ in range(depth - 2):
            for _ in range(len(q)):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        for node in q:
            node.left = TreeNode(val, node.left, None)
            node.right = TreeNode(val, None, node.right)
        return root
