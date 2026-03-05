# You are given a perfect binary tree where all leaves are on the same level,
# and every parent has two children.
# Populate each next pointer to point to its next right node.
# If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.

# Example 1:
# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]

# Example 2:
# Input: root = []
# Output: []

# Constraints:
# The number of nodes in the tree is in the range [0, 2^12 - 1].
# -1000 <= Node.val <= 1000

# Author: Kaustav Ghosh

class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    def connect(self, root):
        if not root:
            return root
        leftmost = root
        while leftmost.left:
            curr = leftmost
            while curr:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                curr = curr.next
            leftmost = leftmost.left
        return root
