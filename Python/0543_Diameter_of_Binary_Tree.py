# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter is the length of the longest path between any two nodes (may or may not pass root).

# Author: Kaustav Ghosh

class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.res = 0
        def depth(node):
            if not node: return 0
            l, r = depth(node.left), depth(node.right)
            self.res = max(self.res, l + r)
            return 1 + max(l, r)
        depth(root)
        return self.res
