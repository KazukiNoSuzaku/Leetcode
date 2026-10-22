# Author: Kaustav Ghosh
# Problem: Merge In Between Linked Lists
# Approach: Only two pointers actually change, so there is no need to rebuild anything: the node just before position a must point at the head of the second list, and the tail of the second list must point at the node just after position b. One walk collects the node before a and, continuing from there, the node after b, and a separate walk to the end of the second list finds its tail. The removed stretch is simply left unreferenced.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


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
            after = after.next

        tail = list2
        while tail.next:
            tail = tail.next

        before.next = list2
        tail.next = after
        return list1
