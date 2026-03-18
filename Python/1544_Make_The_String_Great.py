# Author: Kaustav Ghosh
# Problem: 1544 - Make The String Great
# Approach: Stack: pop if top and current differ only by case

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
