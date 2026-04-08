# Author: Kaustav Ghosh
# Problem: 2236. Root Equals Sum of Children
# URL: https://leetcode.com/problems/root-equals-sum-of-children/
# Difficulty: Easy
#
# Approach:
# Check if the root's value equals the sum of its left and right children.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def checkTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return root.val == root.left.val + root.right.val
