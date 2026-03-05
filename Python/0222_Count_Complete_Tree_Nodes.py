# Given the root of a complete binary tree, return the number of the nodes in the tree.
# Design an algorithm that runs in less than O(n) time complexity.

# Example 1:
# Input: root = [1,2,3,4,5,6]
# Output: 6

# Example 2:
# Input: root = []
# Output: 0

# Constraints:
# The number of nodes in the tree is in the range [0, 5 * 10^4].
# 0 <= Node.val <= 5 * 10^4
# The tree is guaranteed to be complete.

# Author: Kaustav Ghosh

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0
        left_depth = right_depth = 0
        left = right = root
        while left:
            left_depth += 1
            left = left.left
        while right:
            right_depth += 1
            right = right.right
        if left_depth == right_depth:
            return (1 << left_depth) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
