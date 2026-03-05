# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# Return true if there is a cycle in the linked list. Otherwise, return false.

# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true

# Example 2:
# Input: head = [1,2], pos = 0
# Output: true

# Example 3:
# Input: head = [1], pos = -1
# Output: false

# Constraints:
# The number of the nodes in the list is in the range [0, 10^4].
# -10^5 <= Node.val <= 10^5
# pos is -1 or a valid index in the linked-list.

# Author: Kaustav Ghosh

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
