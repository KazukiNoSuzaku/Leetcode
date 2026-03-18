# Author: Kaustav Ghosh
# Problem: 1597 - Build Binary Expression Tree From Infix Expression (Premium)
# Approach: Stack-based infix parsing with operator precedence

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
        def precedence(op):
            if op in ('+', '-'):
                return 1
            if op in ('*', '/'):
                return 2
            return 0

        num_stack = []
        op_stack = []

        def apply_op():
            op = op_stack.pop()
            right = num_stack.pop()
            left = num_stack.pop()
            node = Node(op, left, right)
            num_stack.append(node)

        for c in s:
            if c.isdigit():
                num_stack.append(Node(c))
            elif c == '(':
                op_stack.append(c)
            elif c == ')':
                while op_stack[-1] != '(':
                    apply_op()
                op_stack.pop()
            else:
                while op_stack and op_stack[-1] != '(' and precedence(op_stack[-1]) >= precedence(c):
                    apply_op()
                op_stack.append(c)

        while op_stack:
            apply_op()

        return num_stack[0]
