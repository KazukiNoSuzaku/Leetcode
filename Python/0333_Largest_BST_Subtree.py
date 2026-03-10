# Given the root of a binary tree, find the largest subtree which is a Binary Search Tree (BST),
# where the largest means subtree has the largest number of nodes.
# Return the number of nodes in the largest BST subtree.

# Example 1:
# Input: root = [10,5,15,1,8,null,7]
# Output: 3
# Explanation: The Largest BST Subtree is the highlighted one. The return value is the subtree's size, 3.

# Example 2:
# Input: root = [4,2,7,2,3,5,null,2,null,null,null,null,null,1]
# Output: 2

# Constraints:
# The number of nodes in the tree is in the range [0, 10^4].
# 0 <= Node.val <= 10^4

# Author: Kaustav Ghosh

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def largestBSTSubtree(self, root):
        self.res = 0

        def helper(node):
            # returns (is_bst, size, min_val, max_val)
            if not node:
                return True, 0, float('inf'), float('-inf')
            l_bst, l_size, l_min, l_max = helper(node.left)
            r_bst, r_size, r_min, r_max = helper(node.right)
            if l_bst and r_bst and l_max < node.val < r_min:
                size = l_size + r_size + 1
                self.res = max(self.res, size)
                return True, size, min(l_min, node.val), max(r_max, node.val)
            return False, 0, 0, 0

        helper(root)
        return self.res
