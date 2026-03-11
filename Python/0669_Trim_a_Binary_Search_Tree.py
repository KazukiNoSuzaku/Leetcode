# Trim a BST so all nodes are within [low, high].

# Author: Kaustav Ghosh

class Solution(object):
    def trimBST(self, root, low, high):
        if not root: return None
        if root.val < low: return self.trimBST(root.right, low, high)
        if root.val > high: return self.trimBST(root.left, low, high)
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root
