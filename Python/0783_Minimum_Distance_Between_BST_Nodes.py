# Find minimum difference between any two nodes in a BST.

# Author: Kaustav Ghosh

class Solution(object):
    def minDiffInBST(self, root):
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
