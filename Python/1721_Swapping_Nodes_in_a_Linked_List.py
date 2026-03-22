# Author: Kaustav Ghosh
# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # Find kth node from beginning
        first = head
        for _ in range(k - 1):
            first = first.next

        # Find kth node from end using two pointers
        second = head
        current = first
        while current.next:
            current = current.next
            second = second.next

        # Swap values
        first.val, second.val = second.val, first.val
        return head
