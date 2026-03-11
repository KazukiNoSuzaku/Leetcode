# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between
# the values of any two different nodes in the tree.

# Author: Kaustav Ghosh

class Solution(object):
    def getMinimumDifference(self, root):
        self.prev = None
        self.res = float('inf')
        def inorder(node):
            if not node: return
            inorder(node.left)
            if self.prev is not None:
                self.res = min(self.res, node.val - self.prev)
            self.prev = node.val
            inorder(node.right)
        inorder(root)
        return self.res
