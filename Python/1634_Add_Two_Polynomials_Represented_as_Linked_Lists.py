# Author: Kaustav Ghosh
# Problem: Add Two Polynomials Represented as Linked Lists
# Approach: Both lists are already in strictly descending order of power, so adding them is the merge step of a merge sort: whichever head has the higher power is emitted, and when the powers agree the coefficients are summed. The one wrinkle is that a cancelling pair must emit nothing at all, since the standard form omits zero coefficients, which is why the sum is tested before a node is created. I build fresh nodes rather than splicing the inputs, so neither argument is mutated and no node ends up shared between the inputs and the result, and a dummy head removes the special case for the first term.

# Definition for polynomial singly-linked list.
# class PolyNode(object):
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next


class Solution(object):
    def addPoly(self, poly1, poly2):
        """
        :type poly1: PolyNode
        :type poly2: PolyNode
        :rtype: PolyNode
        """
        dummy = PolyNode()
        tail = dummy
        while poly1 and poly2:
            if poly1.power > poly2.power:
                tail.next = PolyNode(poly1.coefficient, poly1.power)
                tail = tail.next
                poly1 = poly1.next
            elif poly1.power < poly2.power:
                tail.next = PolyNode(poly2.coefficient, poly2.power)
                tail = tail.next
                poly2 = poly2.next
            else:
                combined = poly1.coefficient + poly2.coefficient
                if combined:
                    tail.next = PolyNode(combined, poly1.power)
                    tail = tail.next
                poly1 = poly1.next
                poly2 = poly2.next
        remaining = poly1 or poly2
        while remaining:
            tail.next = PolyNode(remaining.coefficient, remaining.power)
            tail = tail.next
            remaining = remaining.next
        return dummy.next
