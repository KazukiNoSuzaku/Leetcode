# Given a binary tree, populate each next pointer to point to its next right node.
# If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.

# Example 1:
# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]

# Example 2:
# Input: root = []
# Output: []

# Constraints:
# The number of nodes in the tree is in the range [0, 6000].
# -100 <= Node.val <= 100

# Author: Kaustav Ghosh

class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    def connect(self, root):
        curr = root
        while curr:
            dummy = Node(0)
            tail = dummy
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                curr = curr.next
            curr = dummy.next
        return root
