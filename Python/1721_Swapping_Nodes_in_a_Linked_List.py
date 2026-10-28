# Author: Kaustav Ghosh
# Problem: Swapping Nodes in a Linked List
# Approach: The length is unknown up front, but the node k places from the end can be located without measuring it: a pointer set k nodes ahead of another keeps that gap as both advance, so when the leader runs off the end the follower is sitting exactly k from the back. That gives both nodes in one pass. Exchanging their values rather than relinking them avoids all the pointer surgery around adjacency and the case where the two nodes coincide, and leaves the list identical to what relinking would produce.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        leader = head
        for _ in range(k - 1):
            leader = leader.next
        front = leader                 # the k-th node from the start

        follower = head
        leader = leader.next
        while leader:
            leader = leader.next
            follower = follower.next
        back = follower                # the k-th node from the end

        front.val, back.val = back.val, front.val
        return head
