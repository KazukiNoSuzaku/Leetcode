# Author: Kaustav Ghosh
# Problem: Minimum Cost to Change the Final Value of Expression
# Approach: Evaluate with two stacks, carrying for each subexpression the min cost to make it 0 and to make it 1. Combining considers the current operator and a one-cost operator flip; the answer is the nonzero cost of the whole expression

class Solution(object):
    def minOperationsToFlip(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        def op_and(l, r):
            return (min(l[0] + r[0], l[0] + r[1], l[1] + r[0]), l[1] + r[1])

        def op_or(l, r):
            return (l[0] + r[0], min(l[1] + r[1], l[1] + r[0], l[0] + r[1]))

        def combine(l, r, ch):
            a = op_and(l, r)
            o = op_or(l, r)
            if ch == '&':
                return (min(a[0], o[0] + 1), min(a[1], o[1] + 1))
            return (min(o[0], a[0] + 1), min(o[1], a[1] + 1))

        vals = []
        ops = []

        def apply():
            right = vals.pop()
            left = vals.pop()
            vals.append(combine(left, right, ops.pop()))

        for c in expression:
            if c == '0':
                vals.append((0, 1))   # cost to make 0, cost to make 1
            elif c == '1':
                vals.append((1, 0))
            elif c == '(':
                ops.append(c)
            elif c == ')':
                while ops[-1] != '(':
                    apply()
                ops.pop()
            else:  # & or |
                while ops and ops[-1] != '(':
                    apply()
                ops.append(c)

        while ops:
            apply()

        cost0, cost1 = vals[0]
        return max(cost0, cost1)  # one of the two is 0 (the current value)
