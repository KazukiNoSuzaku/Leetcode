# Given the root of a binary tree, return the length of the longest consecutive sequence path.
# A consecutive sequence path is a path where the values increase by one along the path.
# Note that the path can start at any node in the tree, and you can only go from parent nodes to child nodes.

# Example 1:
# Input: root = [1,null,3,2,4,null,null,null,5]
# Output: 3

# Example 2:
# Input: root = [2,null,3,2,null,1]
# Output: 2

# Constraints:
# The number of nodes in the tree is in the range [1, 3 * 10^4].
# -3 * 10^4 <= Node.val <= 3 * 10^4

# Author: Kaustav Ghosh

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def longestConsecutive(self, root):
        self.res = 0
        def dfs(node, parent_val, length):
            if not node:
                return
            length = length + 1 if node.val == parent_val + 1 else 1
            self.res = max(self.res, length)
            dfs(node.left, node.val, length)
            dfs(node.right, node.val, length)
        dfs(root, root.val - 1, 0)
        return self.res
