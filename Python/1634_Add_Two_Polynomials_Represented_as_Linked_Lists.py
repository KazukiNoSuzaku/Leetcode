# Author: Kaustav Ghosh
# Problem: Add Two Polynomials Represented as Linked Lists (Premium)
# Approach: Merge the two power-sorted lists like merge-sort; on equal powers add coefficients and drop the term if the sum is zero

class PolyNode(object):
    def __init__(self, x=0, y=0, next=None):
        self.coefficient = x
        self.power = y
        self.next = next


class Solution(object):
    def addPoly(self, poly1, poly2):
        """
        :type poly1: PolyNode
        :type poly2: PolyNode
        :rtype: PolyNode
        """
        dummy = PolyNode()
        tail = dummy
        p, q = poly1, poly2

        while p and q:
            if p.power > q.power:
                tail.next = PolyNode(p.coefficient, p.power)
                tail = tail.next
                p = p.next
            elif p.power < q.power:
                tail.next = PolyNode(q.coefficient, q.power)
                tail = tail.next
                q = q.next
            else:
                total = p.coefficient + q.coefficient
                if total != 0:
                    tail.next = PolyNode(total, p.power)
                    tail = tail.next
                p = p.next
                q = q.next

        rest = p or q
        while rest:
            tail.next = PolyNode(rest.coefficient, rest.power)
            tail = tail.next
            rest = rest.next

        return dummy.next
