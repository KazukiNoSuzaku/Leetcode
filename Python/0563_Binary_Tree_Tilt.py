# Given the root of a binary tree, return the sum of every tree node's tilt.
# The tilt of a tree node is the absolute difference between the sum of all left subtree
# node values and all right subtree node values.

# Author: Kaustav Ghosh

class Solution(object):
    def findTilt(self, root):
        self.res = 0
        def subtree_sum(node):
            if not node: return 0
            l, r = subtree_sum(node.left), subtree_sum(node.right)
            self.res += abs(l - r)
            return node.val + l + r
        subtree_sum(root)
        return self.res
