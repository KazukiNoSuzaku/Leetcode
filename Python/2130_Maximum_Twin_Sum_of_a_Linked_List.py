# Author: Kaustav Ghosh
# Problem: Maximum Twin Sum of a Linked List
# Approach: Collect the node values, then pair each front element with its mirror from the back and take the maximum of those twin sums

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        vals = []
        cur = head
        while cur:
            vals.append(cur.val)
            cur = cur.next
        n = len(vals)
        return max(vals[i] + vals[n - 1 - i] for i in range(n // 2))
