# Evaluate expression with +, -, *, / and nested parentheses.

# Author: Kaustav Ghosh

class Solution(object):
    def calculate(self, s):
        i = [0]
        def helper():
            stack = []
            op = '+'
            num = 0
            while i[0] < len(s):
                c = s[i[0]]
                i[0] += 1
                if c.isdigit():
                    num = num * 10 + int(c)
                if c == '(':
                    num = helper()
                if (not c.isdigit() and c != ' ') or i[0] == len(s):
                    if op == '+': stack.append(num)
                    elif op == '-': stack.append(-num)
                    elif op == '*': stack.append(stack.pop() * num)
                    elif op == '/': stack.append(int(stack.pop() / num))
                    op = c
                    num = 0
                if c == ')': break
            return sum(stack)
        return helper()
