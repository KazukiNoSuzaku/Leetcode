# Given the root of a binary tree, return the sum of all left leaves.
# A leaf is a node with no children. A left leaf is a leaf that is the left child.

# Author: Kaustav Ghosh

class Solution(object):
    def sumOfLeftLeaves(self, root):
        def dfs(node, is_left):
            if not node:
                return 0
            if not node.left and not node.right:
                return node.val if is_left else 0
            return dfs(node.left, True) + dfs(node.right, False)
        return dfs(root, False)
