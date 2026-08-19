# Author: Kaustav Ghosh
# Problem: Reverse Nodes in Even Length Groups
# Approach: Collect the node values, walk them in groups of sizes 1, 2, 3, ... (the last possibly short), and reverse the values within any group whose actual length is even. Write the values back onto the nodes

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseEvenLengthGroups(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        n = len(nodes)
        start = 0
        group = 1
        while start < n:
            length = min(group, n - start)
            if length % 2 == 0:
                lo, hi = start, start + length - 1
                while lo < hi:
                    nodes[lo].val, nodes[hi].val = nodes[hi].val, nodes[lo].val
                    lo += 1
                    hi -= 1
            start += length
            group += 1
        return head
