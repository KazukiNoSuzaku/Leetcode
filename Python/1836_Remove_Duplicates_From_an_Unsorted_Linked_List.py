# Author: Kaustav Ghosh
# Problem 1836: Remove Duplicates From an Unsorted Linked List (Premium)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicatesUnsorted(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        from collections import Counter
        counts = Counter()
        curr = head
        while curr:
            counts[curr.val] += 1
            curr = curr.next
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        while curr:
            if counts[curr.val] > 1:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next
