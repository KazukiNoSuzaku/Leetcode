# Author: Kaustav Ghosh
# Problem: Sort Linked List Already Sorted Using Absolute Values
# Approach: Sorted by absolute value, the negatives appear in decreasing real value. Walking once and moving each negative node to the front reverses them into ascending order, leaving the whole list sorted by real value

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def sortLinkedList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        prev = head
        cur = head.next
        while cur:
            if cur.val < 0:
                prev.next = cur.next        # detach cur
                cur.next = head             # prepend
                head = cur
                cur = prev.next
            else:
                prev = cur
                cur = cur.next
        return head
