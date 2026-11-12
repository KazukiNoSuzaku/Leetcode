# Author: Kaustav Ghosh
# Problem: Minimum Cost to Change the Final Value of Expression
# Approach: For every subexpression what matters is the cheapest way to force it to zero and the cheapest way to force it to one; whichever matches its natural value costs nothing, and the other is its flip price. Combining two children under an operator means trying the ways each side can supply the needed value, and because an operator itself may be swapped for one extra operation, each combination is also costed as if the other operator were in place. A single left-to-right pass with a stack builds this bottom up: digits push a leaf, a closing bracket collapses the group inside, and a pending operator immediately folds the two neighbouring results together, which also gives the required left-to-right grouping without any precedence rules. No recursion is used, so an expression of a hundred thousand characters cannot overflow the stack.

class Solution(object):
    def minOperationsToFlip(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        def combine(left, right, operator):
            (a0, a1), (b0, b1) = left, right
            and_zero = min(a0 + b0, a0 + b1, a1 + b0)
            and_one = a1 + b1
            or_zero = a0 + b0
            or_one = min(a1 + b0, a0 + b1, a1 + b1)
            if operator == "&":
                return min(and_zero, 1 + or_zero), min(and_one, 1 + or_one)
            return min(or_zero, 1 + and_zero), min(or_one, 1 + and_one)

        stack = []
        for character in expression:
            if character == "(" or character == "&" or character == "|":
                stack.append(character)
                continue
            if character == "0":
                node = (0, 1)
            elif character == "1":
                node = (1, 0)
            else:                       # ')' closes a group
                node = stack.pop()
                stack.pop()             # discard the matching '('
            if stack and (stack[-1] == "&" or stack[-1] == "|"):
                operator = stack.pop()
                node = combine(stack.pop(), node, operator)
            stack.append(node)

        # One of the two costs is zero, the natural value; the other is the answer.
        return max(stack[-1])
