# Return true if the string s can be built by repeatedly inserting "abc"
# into another valid string (starting from empty).

# Author: Kaustav Ghosh

class Solution(object):
    def isValid(self, s):
        stack = []
        for c in s:
            stack.append(c)
            if len(stack) >= 3 and stack[-3:] == ['a', 'b', 'c']:
                stack[-3:] = []
        return len(stack) == 0
