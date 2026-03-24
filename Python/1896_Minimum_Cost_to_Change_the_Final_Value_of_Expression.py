# Author: Kaustav Ghosh
# https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression/

class Solution(object):
    def minOperationsToFlip(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        # Stack-based approach: each element is (value, cost_to_flip)
        stack = []
        ops = []
        for ch in expression:
            if ch == '(' :
                ops.append(ch)
            elif ch == '0':
                stack.append((0, 1))
            elif ch == '1':
                stack.append((1, 1))
            elif ch in '&|':
                ops.append(ch)
            elif ch == ')':
                # Pop until matching '('
                while ops and ops[-1] != '(':
                    op = ops.pop()
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(self._combine(a, b, op))
                ops.pop()  # remove '('
            # After pushing, combine if top of ops is & or |
            while len(stack) >= 2 and ops and ops[-1] in '&|':
                op = ops.pop()
                b = stack.pop()
                a = stack.pop()
                stack.append(self._combine(a, b, op))
        return stack[0][1]

    def _combine(self, a, b, op):
        """
        :type a: tuple (value, cost)
        :type b: tuple (value, cost)
        :type op: str
        :rtype: tuple
        """
        va, ca = a
        vb, cb = b
        if op == '&':
            if va == 0 and vb == 0:
                return (0, min(ca, cb))
            elif va == 0 and vb == 1:
                return (0, 1)
            elif va == 1 and vb == 0:
                return (0, 1)
            else:  # 1 & 1
                return (1, min(ca, cb) + 1)
        else:  # op == '|'
            if va == 0 and vb == 0:
                return (0, min(ca, cb) + 1)
            elif va == 0 and vb == 1:
                return (1, 1)
            elif va == 1 and vb == 0:
                return (1, 1)
            else:  # 1 | 1
                return (1, min(ca, cb))
