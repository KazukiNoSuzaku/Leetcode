# Author: Kaustav Ghosh
# Problem 2074: Reverse Nodes in Even Length Groups

class Solution(object):
    def reverseEvenLengthGroups(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Collect all values
        vals = []
        node = head
        while node:
            vals.append(node.val)
            node = node.next

        # Process groups
        idx = 0
        group = 1
        while idx < len(vals):
            size = min(group, len(vals) - idx)
            if size % 2 == 0:
                vals[idx:idx + size] = vals[idx:idx + size][::-1]
            idx += size
            group += 1

        # Write values back
        node = head
        for v in vals:
            node.val = v
            node = node.next
        return head
