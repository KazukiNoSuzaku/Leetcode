# Author: Kaustav Ghosh
# Problem: Design an Expression Tree With Evaluate Function (Premium)
# Approach: Read postfix with a stack; operands become leaves, operators pop two subtrees. evaluate() recurses, dividing with truncation toward zero

from abc import ABC, abstractmethod

class Node(ABC):
    @abstractmethod
    def evaluate(self):
        pass


class NumNode(Node):
    def __init__(self, val):
        self.val = val

    def evaluate(self):
        return self.val


class OpNode(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def evaluate(self):
        a = self.left.evaluate()
        b = self.right.evaluate()
        if self.op == '+':
            return a + b
        if self.op == '-':
            return a - b
        if self.op == '*':
            return a * b
        return int(a / b)  # truncate toward zero


class TreeBuilder(object):
    def buildTree(self, postfix):
        """
        :type postfix: List[str]
        :rtype: Node
        """
        stack = []
        for token in postfix:
            if token in ('+', '-', '*', '/'):
                right = stack.pop()
                left = stack.pop()
                stack.append(OpNode(token, left, right))
            else:
                stack.append(NumNode(int(token)))
        return stack[-1]
