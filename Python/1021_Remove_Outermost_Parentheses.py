# Remove the outermost parentheses of every primitive decomposition.

# Author: Kaustav Ghosh

class Solution(object):
    def removeOuterParentheses(self, s):
        res = []
        depth = 0
        for c in s:
            if c == '(' and depth > 0: res.append(c)
            if c == ')' and depth > 1: res.append(c)
            depth += 1 if c == '(' else -1
        return ''.join(res)
