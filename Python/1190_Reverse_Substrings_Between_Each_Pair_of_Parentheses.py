# Author: Kaustav Ghosh
# Stack-based: on '(' push current string, on ')' reverse and concatenate

class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = [[]]
        for ch in s:
            if ch == '(':
                stack.append([])
            elif ch == ')':
                top = stack.pop()
                top.reverse()
                stack[-1].extend(top)
            else:
                stack[-1].append(ch)
        return ''.join(stack[0])
