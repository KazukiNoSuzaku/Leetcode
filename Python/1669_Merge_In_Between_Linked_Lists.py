# Author: Kaustav Ghosh
# Problem: Merge In Between Linked Lists
# Approach: Find the node before index a and the node after index b, then splice list2 between them

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        before = list1
        for _ in range(a - 1):
            before = before.next

        after = before
        for _ in range(b - a + 2):
            after = after.next  # node right after index b

        before.next = list2
        tail = list2
        while tail.next:
            tail = tail.next
        tail.next = after
        return list1
