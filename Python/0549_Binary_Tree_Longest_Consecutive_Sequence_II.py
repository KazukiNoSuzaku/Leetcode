# Given the root of a binary tree, return the length of the longest consecutive path in the tree.
# The path can be in increasing or decreasing consecutive values (need not pass through root).

# Author: Kaustav Ghosh

class Solution(object):
    def longestConsecutive(self, root):
        self.res = 0
        def dfs(node):
            if not node: return 0, 0  # inc, dec length ending at node
            li, ld = dfs(node.left)
            ri, rd = dfs(node.right)
            inc = dec = 1
            if node.left:
                if node.left.val == node.val + 1: inc = max(inc, li + 1)
                if node.left.val == node.val - 1: dec = max(dec, ld + 1)
            if node.right:
                if node.right.val == node.val + 1: inc = max(inc, ri + 1)
                if node.right.val == node.val - 1: dec = max(dec, rd + 1)
            self.res = max(self.res, inc + dec - 1)
            return inc, dec
        dfs(root)
        return self.res
