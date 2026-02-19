# Given the head of a linked list and a value x, partition it such that all nodes less than x
# come before nodes greater than or equal to x.
# Preserve the original relative order of the nodes in each of the two partitions.

# Example 1:
# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]

# Example 2:
# Input: head = [2,1], x = 2
# Output: [1,2]

# Constraints:
# The number of nodes in the list is in the range [0, 200].
# -100 <= Node.val <= 100
# -200 <= x <= 200

# Author: Kaustav Ghosh

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def partition(self, head, x):
        before_head = ListNode(0)
        after_head = ListNode(0)
        before = before_head
        after = after_head

        curr = head
        while curr:
            if curr.val < x:
                before.next = curr
                before = before.next
            else:
                after.next = curr
                after = after.next
            curr = curr.next

        after.next = None
        before.next = after_head.next
        return before_head.next
