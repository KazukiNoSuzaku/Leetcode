# Given the root of a binary tree, construct a string consisting of parenthesis and integers
# from a binary tree with the preorder traversal way, and return it.
# Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship.

# Author: Kaustav Ghosh

class Solution(object):
    def tree2str(self, root):
        if not root: return ''
        res = str(root.val)
        if root.left or root.right:
            res += '(' + self.tree2str(root.left) + ')'
        if root.right:
            res += '(' + self.tree2str(root.right) + ')'
        return res
