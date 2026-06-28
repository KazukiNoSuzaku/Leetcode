# Author: Kaustav Ghosh
# Problem: Make The String Great
# Approach: Use a stack; pop when the top and current char are the same letter in opposite case, else push

class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for c in s:
            if stack and stack[-1] != c and stack[-1].lower() == c.lower():
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)
