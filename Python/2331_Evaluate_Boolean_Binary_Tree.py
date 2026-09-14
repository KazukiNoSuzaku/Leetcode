# Author: Kaustav Ghosh
# Problem: Evaluate Boolean Binary Tree
# Approach: Recursively evaluate the tree. Leaves are boolean values (0/1); internal nodes are operators (2 = OR, 3 = AND) combining their two children's evaluated results

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def evaluateTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root.left is None and root.right is None:
            return root.val == 1
        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)
        if root.val == 2:
            return left or right
        return left and right
