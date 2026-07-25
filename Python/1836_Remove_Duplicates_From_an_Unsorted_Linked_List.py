# Author: Kaustav Ghosh
# Problem: Remove Duplicates From an Unsorted Linked List (Premium)
# Approach: One pass to count each value, a second pass with a dummy head to unlink every node whose value appeared more than once

from collections import Counter

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicatesUnsorted(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        counts = Counter()
        node = head
        while node:
            counts[node.val] += 1
            node = node.next

        dummy = ListNode(0, head)
        prev = dummy
        node = head
        while node:
            if counts[node.val] > 1:
                prev.next = node.next  # unlink duplicate
            else:
                prev = node
            node = node.next
        return dummy.next
