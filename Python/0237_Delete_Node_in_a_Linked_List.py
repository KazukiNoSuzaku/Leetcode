# There is a singly-linked list and you are given access to a node to be deleted.
# The node to be deleted is not a tail node. Delete the given node.
# You will not be given access to the head of the list.

# Example 1:
# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]

# Example 2:
# Input: head = [4,5,1,9], node = 1
# Output: [4,5,9]

# Constraints:
# The number of nodes in the given list is in the range [2, 1000].
# -1000 <= Node.val <= 1000
# The value of each node in the list is unique.
# The node to be deleted is not a tail node.

# Author: Kaustav Ghosh

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
