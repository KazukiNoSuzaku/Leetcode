# Author: Kaustav Ghosh
# 2331. Evaluate Boolean Binary Tree
# https://leetcode.com/problems/evaluate-boolean-binary-tree/
# Recursively evaluate: leaf returns val, OR/AND nodes recurse left and right

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def evaluateTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root.left is None and root.right is None:
            return bool(root.val)
        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)
        if root.val == 2:
            return left or right
        else:  # root.val == 3
            return left and right
