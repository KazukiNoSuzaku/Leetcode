# You are given the root of a binary tree containing digits from 0 to 9 only.
# Each root-to-leaf path in the tree represents a number.
# Given the root of the tree, return the total sum of all root-to-leaf numbers.

# Example 1:
# Input: root = [1,2,3]
# Output: 25
# Explanation: 1->2 represents 12, 1->3 represents 13. Sum = 12 + 13 = 25.

# Example 2:
# Input: root = [4,9,0,5,1]
# Output: 1026
# Explanation: 4->9->5 = 495, 4->9->1 = 491, 4->0 = 40. Sum = 495 + 491 + 40 = 1026.

# Constraints:
# The number of nodes in the tree is in the range [1, 1000].
# 0 <= Node.val <= 9
# The depth of the tree will not exceed 10.

# Author: Kaustav Ghosh

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sumNumbers(self, root):
        def dfs(node, curr):
            if not node:
                return 0
            curr = curr * 10 + node.val
            if not node.left and not node.right:
                return curr
            return dfs(node.left, curr) + dfs(node.right, curr)
        return dfs(root, 0)
