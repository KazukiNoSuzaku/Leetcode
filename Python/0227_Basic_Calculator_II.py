# Given a string s which represents an expression, evaluate this expression and return its value.
# The integer division should truncate toward zero.
# s contains '+', '-', '*', '/' operators and non-negative integers.

# Example 1:
# Input: s = "3+2*2"
# Output: 7

# Example 2:
# Input: s = " 3/2 "
# Output: 1

# Example 3:
# Input: s = " 3+5 / 2 "
# Output: 5

# Constraints:
# 1 <= s.length <= 3 * 10^5
# s consists of integers and operators ('+', '-', '*', '/'), separated by spaces.

# Author: Kaustav Ghosh

class Solution(object):
    def calculate(self, s):
        stack = []
        num = 0
        op = '+'
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            if (not c.isdigit() and c != ' ') or i == len(s) - 1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                elif op == '/':
                    stack.append(int(stack.pop() / num))
                op = c
                num = 0
        return sum(stack)
