# Author: Kaustav Ghosh
# Problem: Binary Search Tree Iterator II
# Approach: Flattening the whole tree in the constructor would answer the follow-up badly and would also recurse a hundred thousand levels deep on a degenerate tree, so instead I keep the usual iterative in-order stack holding the leftmost spine of the unvisited part, plus a growing list of the values already handed out and a cursor into it. Moving back is just a step of the cursor, and moving forward either revisits a value already recorded or, when the cursor is at the frontier, advances the stack by one node and appends it. So nothing is computed until it is asked for, and every call costs amortised constant time.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.visited = []
        self.cursor = -1
        self._descend(root)

    def _descend(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cursor + 1 < len(self.visited) or bool(self.stack)

    def next(self):
        """
        :rtype: int
        """
        self.cursor += 1
        if self.cursor == len(self.visited):
            node = self.stack.pop()
            self.visited.append(node.val)
            self._descend(node.right)
        return self.visited[self.cursor]

    def hasPrev(self):
        """
        :rtype: bool
        """
        return self.cursor > 0

    def prev(self):
        """
        :rtype: int
        """
        self.cursor -= 1
        return self.visited[self.cursor]


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.hasNext()
# param_2 = obj.next()
# param_3 = obj.hasPrev()
# param_4 = obj.prev()
