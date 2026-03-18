# Author: Kaustav Ghosh
# Problem: 1586 - Binary Search Tree Iterator II (Premium)
# Approach: Controlled inorder with stack; maintain list of visited nodes for prev()

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.visited = []
        self.index = -1
        self._push_left(root)

    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index < len(self.visited) - 1 or len(self.stack) > 0

    def next(self):
        """
        :rtype: int
        """
        self.index += 1
        if self.index < len(self.visited):
            return self.visited[self.index]
        node = self.stack.pop()
        self.visited.append(node.val)
        self._push_left(node.right)
        return node.val

    def hasPrev(self):
        """
        :rtype: bool
        """
        return self.index > 0

    def prev(self):
        """
        :rtype: int
        """
        self.index -= 1
        return self.visited[self.index]
