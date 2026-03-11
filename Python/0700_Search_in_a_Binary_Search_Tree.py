# Find the node with value val in a BST and return its subtree.

# Author: Kaustav Ghosh

class Solution(object):
    def searchBST(self, root, val):
        while root:
            if val == root.val: return root
            root = root.left if val < root.val else root.right
        return None
