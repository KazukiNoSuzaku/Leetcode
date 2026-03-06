# Given the root of a binary search tree and a target value, return the value in the BST
# that is closest to the target. If there are multiple answers, print the smallest.

# Example 1:
# Input: root = [4,2,5,1,3], target = 3.714286
# Output: 4

# Example 2:
# Input: root = [1], target = 4.428571
# Output: 1

# Constraints:
# The number of nodes in the tree is in the range [1, 10^4].
# 0 <= Node.val <= 10^9
# -10^9 <= target <= 10^9

# Author: Kaustav Ghosh

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def closestValue(self, root, target):
        closest = root.val
        node = root
        while node:
            if abs(node.val - target) < abs(closest - target):
                closest = node.val
            if target < node.val:
                node = node.left
            else:
                node = node.right
        return closest
