# Author: Kaustav Ghosh
# Problem: Swapping Nodes in a Linked List
# Approach: Walk k-1 steps to the first node, then advance a runner and a second pointer together so the second lands on the kth from the end; swap their values

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        first = head
        for _ in range(k - 1):
            first = first.next

        second = head
        runner = first
        while runner.next:
            runner = runner.next
            second = second.next

        first.val, second.val = second.val, first.val
        return head
