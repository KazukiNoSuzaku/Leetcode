# Given two integer arrays inorder and postorder where inorder is the inorder traversal
# of a binary tree and postorder is the postorder traversal of the same tree,
# construct and return the binary tree.

# Example 1:
# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]

# Example 2:
# Input: inorder = [-1], postorder = [-1]
# Output: [-1]

# Constraints:
# 1 <= inorder.length <= 2000
# postorder.length == inorder.length
# -1000 <= inorder[i], postorder[i] <= 1000
# inorder and postorder consist of unique values.

# Author: Kaustav Ghosh

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, inorder, postorder):
        if not postorder:
            return None
        root_val = postorder[-1]
        root = TreeNode(root_val)
        mid = inorder.index(root_val)
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid + 1:], postorder[mid:-1])
        return root
