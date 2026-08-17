# Author: Kaustav Ghosh
# Problem: Find the Minimum and Maximum Number of Nodes Between Critical Points
# Approach: Walk the list tracking each node with its two neighbors; a strict local minimum or maximum is a critical point. Record their positions; the max distance is last minus first, the min distance is the smallest gap between consecutive criticals

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        positions = []
        prev = head
        cur = head.next if head else None
        index = 1
        while cur and cur.next:
            if (cur.val > prev.val and cur.val > cur.next.val) or \
               (cur.val < prev.val and cur.val < cur.next.val):
                positions.append(index)
            prev = cur
            cur = cur.next
            index += 1

        if len(positions) < 2:
            return [-1, -1]

        max_dist = positions[-1] - positions[0]
        min_dist = min(positions[i + 1] - positions[i] for i in range(len(positions) - 1))
        return [min_dist, max_dist]
