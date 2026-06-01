from math import gcd

class Solution:
    def insertGreatestCommonDivisors(self, head):
        curr = head
        while curr.next:
            g = gcd(curr.val, curr.next.val)
            curr.next = ListNode(g, curr.next)
            curr = curr.next.next
        return head
