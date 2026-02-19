# Given an integer n, return all the structurally unique BST's (binary search trees),
# which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

# Example 1:
# Input: n = 3
# Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

# Example 2:
# Input: n = 1
# Output: [[1]]

# Constraints:
# 1 <= n <= 8

# Author: Kaustav Ghosh

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def generateTrees(self, n):
        def generate(start, end):
            if start > end:
                return [None]
            trees = []
            for root_val in range(start, end + 1):
                left_trees = generate(start, root_val - 1)
                right_trees = generate(root_val + 1, end)
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right
                        trees.append(root)
            return trees

        return generate(1, n)
