# Author: Kaustav Ghosh
# Problem: Remove Duplicates From an Unsorted Linked List
# Approach: Whether a node survives depends on how often its value occurs anywhere in the list, not on its neighbours, so no decision can be made during a single pass; the counts are tallied first and the unlinking happens on a second pass. A dummy node in front of the head means the first node is removed by the same two lines as any other, with no special case for the list becoming empty. The predecessor only advances when a node is kept, which keeps a run of duplicates from leaving a stale link behind.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicatesUnsorted(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        from collections import Counter

        occurrences = Counter()
        node = head
        while node:
            occurrences[node.val] += 1
            node = node.next

        dummy = ListNode(0, head)
        previous, node = dummy, head
        while node:
            if occurrences[node.val] > 1:
                previous.next = node.next
            else:
                previous = node
            node = node.next
        return dummy.next
