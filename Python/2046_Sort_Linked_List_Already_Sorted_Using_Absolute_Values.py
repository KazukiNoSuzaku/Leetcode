# Author: Kaustav Ghosh
# Problem: Sort Linked List Already Sorted Using Absolute Values
# Approach: Being sorted by absolute value already places the non-negative nodes in correct ascending order among themselves, and it places the negative nodes in ascending order of magnitude, which is descending order of actual value. Reversing just the negatives and moving them ahead of everything therefore sorts the list, and detaching each negative node as it is met and splicing it onto the front does both at once, because the last negative detached ends up first. The non-negative nodes are simply walked past and keep their relative order, so one pass suffices with no new nodes allocated and no comparisons between values.

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
        previous = head
        current = head.next
        while current:
            if current.val < 0:
                following = current.next
                previous.next = following
                current.next = head
                head = current
                current = following
            else:
                previous = current
                current = current.next
        return head
