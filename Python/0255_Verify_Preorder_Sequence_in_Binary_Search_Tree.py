# Given an array of unique integers preorder, return true if it is the correct preorder traversal
# sequence of a binary search tree.

# Example 1:
# Input: preorder = [5,2,1,3,6]
# Output: true

# Example 2:
# Input: preorder = [5,2,6,1,3]
# Output: false

# Constraints:
# 1 <= preorder.length <= 10^4
# 1 <= preorder[i] <= 10^4
# All the elements of preorder are unique.

# Author: Kaustav Ghosh

class Solution(object):
    def verifyPreorder(self, preorder):
        stack = []
        low = float('-inf')
        for val in preorder:
            if val < low:
                return False
            while stack and stack[-1] < val:
                low = stack.pop()
            stack.append(val)
        return True
