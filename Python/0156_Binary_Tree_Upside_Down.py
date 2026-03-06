# Given the root of a binary tree where every node has either 0 or 2 children, and every right
# node is a leaf node, flip the tree upside down. Turn it into a tree where the original right
# nodes turned into left leaf nodes.
# Return the new root.

# Example 1:
# Input: root = [1,2,3,4,5]
# Output: [4,5,2,null,null,3,1]

# Example 2:
# Input: root = []
# Output: []

# Constraints:
# The number of nodes in the tree will be in the range [0, 10].
# 1 <= Node.val <= 10

# Author: Kaustav Ghosh

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def upsideDownBinaryTree(self, root):
        if not root or not root.left:
            return root
        new_root = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root
        root.left = None
        root.right = None
        return new_root
