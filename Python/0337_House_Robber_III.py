# The thief has found himself a new place for his thievery again. There is only one entrance to
# this area, called root. Besides the root, each house has one and only one parent house.
# The police will be contacted if two directly-linked houses were broken into on the same night.
# Given the root of the binary tree, return the maximum amount of money the thief can rob.

# Example 1:
# Input: root = [3,2,3,null,3,null,1]
# Output: 7

# Example 2:
# Input: root = [3,4,5,1,3,null,1]
# Output: 9

# Constraints:
# The number of nodes in the tree is in the range [1, 10^4].
# 0 <= Node.val <= 10^4

# Author: Kaustav Ghosh

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def rob(self, root):
        def dfs(node):
            if not node:
                return 0, 0  # (rob_this, skip_this)
            lr, ls = dfs(node.left)
            rr, rs = dfs(node.right)
            rob_this = node.val + ls + rs
            skip_this = max(lr, ls) + max(rr, rs)
            return rob_this, skip_this
        return max(dfs(root))
