# Given a string representing a code snippet, implement a tag validator to parse the code
# and return whether the code snippet is valid. Tag rules: CDATA, closed tags, etc.

# Author: Kaustav Ghosh

import re

class Solution(object):
    def isValid(self, code):
        stack = []
        i = 0
        while i < len(code):
            if i > 0 and not stack: return False
            if code[i:i+9] == '<![CDATA[':
                j = code.find(']]>', i + 9)
                if j < 0: return False
                i = j + 3
            elif code[i:i+2] == '</':
                j = code.find('>', i)
                if j < 0: return False
                tag = code[i+2:j]
                if not stack or stack[-1] != tag: return False
                stack.pop()
                i = j + 1
            elif code[i] == '<':
                j = code.find('>', i)
                if j < 0: return False
                tag = code[i+1:j]
                if not re.match(r'^[A-Z]{1,9}$', tag): return False
                stack.append(tag)
                i = j + 1
            else:
                i += 1
        return not stack
