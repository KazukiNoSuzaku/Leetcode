# Author: Kaustav Ghosh
# Problem: Build Binary Expression Tree From Infix Expression
# Approach: This is the shunting-yard algorithm building nodes instead of emitting postfix: digits become leaves pushed on an operand stack, while operators wait on their own stack until an operator of equal or lower precedence arrives, at which point the pending ones are folded into internal nodes. Folding on equal precedence is what makes same-level operators group left to right, so subtraction and division come out the right way round, and an opening parenthesis acts as a floor that nothing folds past until its closing partner arrives. Whatever operators remain at the end are folded in order, leaving the root as the only operand.

# Definition for a binary tree node.
class Node(object):
    def __init__(self, val=" ", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def expTree(self, s):
        """
        :type s: str
        :rtype: Node
        """
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        operands = []
        operators = []

        def fold():
            right = operands.pop()
            left = operands.pop()
            operands.append(Node(operators.pop(), left, right))

        for ch in s:
            if ch.isdigit():
                operands.append(Node(ch))
            elif ch == '(':
                operators.append(ch)
            elif ch == ')':
                while operators[-1] != '(':
                    fold()
                operators.pop()
            else:
                while (operators and operators[-1] != '('
                       and precedence[operators[-1]] >= precedence[ch]):
                    fold()
                operators.append(ch)

        while operators:
            fold()
        return operands[0]
