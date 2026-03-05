# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes
# in the sequence has an edge connecting them. A node can only appear in the sequence at most once.
# Note that the path does not need to pass through the root.
# The path sum of a path is the sum of the node's values in the path.
# Given the root of a binary tree, return the maximum path sum of any non-empty path.

# Example 1:
# Input: root = [1,2,3]
# Output: 6

# Example 2:
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42

# Constraints:
# The number of nodes in the tree is in the range [1, 3 * 10^4].
# -1000 <= Node.val <= 1000

# Author: Kaustav Ghosh

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxPathSum(self, root):
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            self.max_sum = max(self.max_sum, node.val + left + right)
            return node.val + max(left, right)

        dfs(root)
        return self.max_sum
