# Author: Kaustav Ghosh
# Problem: Remove Nodes From Linked List
# Approach: A node survives only if nothing larger follows it, which is exactly what a decreasing stack keeps: push each node, popping any node it beats. The stack then holds the surviving nodes in order, so relink them

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        kept = []
        node = head
        while node:
            while kept and kept[-1].val < node.val:
                kept.pop()
            kept.append(node)
            node = node.next
        for i in range(len(kept) - 1):
            kept[i].next = kept[i + 1]
        if kept:
            kept[-1].next = None
        return kept[0] if kept else None
