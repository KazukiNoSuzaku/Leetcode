# Given string num representing a non-negative integer num, and an integer k,
# return the smallest possible integer after removing k digits from num.

# Author: Kaustav Ghosh

class Solution(object):
    def removeKdigits(self, num, k):
        stack = []
        for d in num:
            while k and stack and stack[-1] > d:
                stack.pop()
                k -= 1
            stack.append(d)
        if k:
            stack = stack[:-k]
        return ''.join(stack).lstrip('0') or '0'
