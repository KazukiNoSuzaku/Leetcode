# Design a complete binary tree inserter using BFS level order.

# Author: Kaustav Ghosh

from collections import deque

class CBTInserter(object):
    def __init__(self, root):
        self.root = root
        self.deque = deque()
        q = deque([root])
        while q:
            node = q.popleft()
            if not node.left or not node.right:
                self.deque.append(node)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

    def insert(self, val):
        parent = self.deque[0]
        node = TreeNode(val)
        if not parent.left: parent.left = node
        else: parent.right = node; self.deque.popleft()
        self.deque.append(node)
        return parent.val

    def get_root(self):
        return self.root
