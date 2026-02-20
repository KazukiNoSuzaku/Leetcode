# Given a binary tree, determine if it is height-balanced.
# A height-balanced binary tree is a binary tree in which the depth of the two subtrees
# of every node never differs by more than one.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Example 2:
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false

# Example 3:
# Input: root = []
# Output: true

# Constraints:
# The number of nodes in the tree is in the range [0, 5000].
# -10^4 <= Node.val <= 10^4

# Author: Kaustav Ghosh

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        def height(node):
            if not node:
                return 0
            left = height(node.left)
            if left == -1:
                return -1
            right = height(node.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
        return height(root) != -1
