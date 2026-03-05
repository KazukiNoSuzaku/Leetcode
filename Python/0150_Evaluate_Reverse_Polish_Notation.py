# You are given an array of strings tokens that represents an arithmetic expression in
# Reverse Polish Notation. Evaluate the expression. Return an integer that represents
# the value of the expression.
# Note that division between two integers should truncate toward zero.

# Example 1:
# Input: tokens = ["2","1","+","3","*"]
# Output: 9

# Example 2:
# Input: tokens = ["4","13","5","/","+"]
# Output: 6

# Example 3:
# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22

# Constraints:
# 1 <= tokens.length <= 10^4
# tokens[i] is either an operator ("+", "-", "*", "/") or an integer.

# Author: Kaustav Ghosh

class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        ops = {'+', '-', '*', '/'}
        for t in tokens:
            if t in ops:
                b, a = stack.pop(), stack.pop()
                if t == '+':
                    stack.append(a + b)
                elif t == '-':
                    stack.append(a - b)
                elif t == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
            else:
                stack.append(int(t))
        return stack[0]
