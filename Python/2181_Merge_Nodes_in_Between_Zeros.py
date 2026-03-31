# Author: Kaustav Ghosh
# 2181. Merge Nodes in Between Zeros
# https://leetcode.com/problems/merge-nodes-in-between-zeros/
# Difficulty: Medium
#
# Approach: Traverse the linked list, accumulating sum between zeros.
# When a zero is encountered (and sum > 0), create a new node with that sum.
# Time: O(n), Space: O(1) extra (output list reuses nodes)

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        tail = dummy
        curr = head.next  # skip the leading zero
        total = 0

        while curr:
            if curr.val == 0:
                tail.next = ListNode(total)
                tail = tail.next
                total = 0
            else:
                total += curr.val
            curr = curr.next

        return dummy.next
