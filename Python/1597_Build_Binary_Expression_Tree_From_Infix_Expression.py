# Author: Kaustav Ghosh
# Problem: Build Binary Expression Tree From Infix Expression (Premium)
# Approach: Shunting-yard with two stacks (operand nodes and operators); pop an operator into a subtree whenever a lower/equal precedence one arrives

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
        prec = {'+': 1, '-': 1, '*': 2, '/': 2}
        nodes, ops = [], []

        def merge():
            op = ops.pop()
            right = nodes.pop()
            left = nodes.pop()
            nodes.append(Node(op, left, right))

        for c in s:
            if c == '(':
                ops.append(c)
            elif c == ')':
                while ops[-1] != '(':
                    merge()
                ops.pop()  # discard '('
            elif c in prec:
                while ops and ops[-1] != '(' and prec[ops[-1]] >= prec[c]:
                    merge()
                ops.append(c)
            else:  # single-digit operand
                nodes.append(Node(c))

        while ops:
            merge()
        return nodes[0]
