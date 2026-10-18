# Author: Kaustav Ghosh
# Problem: Design an Expression Tree With Evaluate Function
# Approach: Postfix means an operator always arrives after both its operands, so one stack rebuilds the tree in a single pass: a number becomes a leaf and an operator pops its right then its left child, which is the order that keeps subtraction and division the right way round. For the follow-up about modularity I split the two kinds of node rather than branching inside one evaluate: a leaf returns its value, and an operator node looks its symbol up in a table of two-argument functions, so supporting a new operator is a single new table entry and no change at all to evaluate. Division truncates toward zero rather than using Python's floor division, matching the integer division of the languages the problem is specified against, which differ for negative quotients.

from abc import ABC, abstractmethod


"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""


class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self):
        pass


class Operand(Node):
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value


def _divide(left, right):
    quotient = abs(left) // abs(right)
    return quotient if (left < 0) == (right < 0) else -quotient


class Operation(Node):
    # Adding an operator means adding one entry here and nothing else.
    APPLY = {
        '+': lambda left, right: left + right,
        '-': lambda left, right: left - right,
        '*': lambda left, right: left * right,
        '/': _divide,
    }

    def __init__(self, symbol, left, right):
        self.symbol = symbol
        self.left = left
        self.right = right

    def evaluate(self):
        return self.APPLY[self.symbol](self.left.evaluate(), self.right.evaluate())


"""
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""


class TreeBuilder(object):
    def buildTree(self, postfix):
        """
        :type postfix: List[str]
        :rtype: Node
        """
        stack = []
        for token in postfix:
            if token in Operation.APPLY:
                right = stack.pop()
                left = stack.pop()
                stack.append(Operation(token, left, right))
            else:
                stack.append(Operand(int(token)))
        return stack.pop()
