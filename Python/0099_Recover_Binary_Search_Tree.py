# You are given the root of a binary search tree (BST), where the values of exactly
# two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

# Example 1:
# Input: root = [1,3,null,null,2]
# Output: [3,1,null,null,2]

# Example 2:
# Input: root = [3,1,4,null,null,2]
# Output: [2,1,4,null,null,3]

# Constraints:
# The number of nodes in the tree is in the range [2, 1000].
# -2^31 <= Node.val <= 2^31 - 1

# Author: Kaustav Ghosh

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def recoverTree(self, root):
        self.first = self.second = self.prev = None

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev and self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev
                self.second = node
            self.prev = node
            inorder(node.right)

        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val
