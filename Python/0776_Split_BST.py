# Split a BST into two trees: one with values <= V and one with values > V.

# Author: Kaustav Ghosh

class Solution(object):
    def splitBST(self, root, target):
        if not root: return [None, None]
        if root.val <= target:
            left, right = self.splitBST(root.right, target)
            root.right = left
            return [root, right]
        else:
            left, right = self.splitBST(root.left, target)
            root.left = right
            return [left, root]
