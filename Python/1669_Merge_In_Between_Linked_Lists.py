# Author: Kaustav Ghosh
# https://leetcode.com/problems/merge-in-between-linked-lists/

class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        curr = list1
        for i in range(a - 1):
            curr = curr.next
        start = curr
        for i in range(b - a + 2):
            curr = curr.next
        end = curr
        start.next = list2
        tail = list2
        while tail.next:
            tail = tail.next
        tail.next = end
        return list1
