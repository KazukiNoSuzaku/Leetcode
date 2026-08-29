# Author: Kaustav Ghosh
# Problem: Merge Nodes in Between Zeros
# Approach: Walk the list accumulating the sum of values between consecutive zeros. Each time a zero boundary is reached, emit a single node holding the accumulated sum. Build the result with a dummy head

# Definition for singly-linked list.
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
        cur = head.next  # skip the leading zero
        acc = 0
        while cur:
            if cur.val == 0:
                tail.next = ListNode(acc)
                tail = tail.next
                acc = 0
            else:
                acc += cur.val
            cur = cur.next
        return dummy.next
