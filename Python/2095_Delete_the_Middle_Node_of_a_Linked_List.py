# Author: Kaustav Ghosh
# Problem: Delete the Middle Node of a Linked List
# Approach: Use slow/fast pointers, keeping the node before slow. When fast reaches the end, slow is the middle (index n//2); unlink it. A single-node list becomes empty

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return None
        prev = None
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        return head
