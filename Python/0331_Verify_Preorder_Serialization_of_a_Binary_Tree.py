# One way to serialize a binary tree is to use preorder traversal. When we encounter a
# non-null node, we record the node's value. If it is a null node, we record using a sentinel
# value such as '#'.
# Given a string of comma-separated values preorder, return true if it is a correct preorder
# traversal serialization of some binary tree.

# Example 1:
# Input: preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
# Output: true

# Example 2:
# Input: preorder = "1,#"
# Output: false

# Constraints:
# 1 <= preorder.length <= 10^4
# preorder consist of integers in the range [0, 100] and '#' separated by commas ','.

# Author: Kaustav Ghosh

class Solution(object):
    def isValidSerialization(self, preorder):
        slots = 1
        for node in preorder.split(','):
            slots -= 1
            if slots < 0:
                return False
            if node != '#':
                slots += 2
        return slots == 0
