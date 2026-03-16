# Author: Kaustav Ghosh
# Problem: Delete N Nodes After M Nodes of a Linked List (Premium)
# Approach: Simulate skip M nodes then delete N nodes

class Solution(object):
    def deleteNodes(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        current = head
        while current:
            for _ in range(m - 1):
                if not current:
                    return head
                current = current.next
            if not current:
                return head
            temp = current
            for _ in range(n):
                if not temp.next:
                    break
                temp.next = temp.next.next
            current = current.next
        return head
