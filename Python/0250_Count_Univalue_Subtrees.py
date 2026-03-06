# Given the root of a binary tree, return the number of uni-value subtrees.
# A uni-value subtree means all nodes of the subtree have the same value.

# Example 1:
# Input: root = [5,1,5,5,5,null,5]
# Output: 4

# Example 2:
# Input: root = []
# Output: 0

# Constraints:
# The number of the node in the tree will be in the range [0, 1000].
# -1000 <= Node.val <= 1000

# Author: Kaustav Ghosh

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def countUnivalSubtrees(self, root):
        self.count = 0
        def is_uni(node):
            if not node:
                return True
            left = is_uni(node.left)
            right = is_uni(node.right)
            if not left or not right:
                return False
            if node.left and node.left.val != node.val:
                return False
            if node.right and node.right.val != node.val:
                return False
            self.count += 1
            return True
        is_uni(root)
        return self.count
