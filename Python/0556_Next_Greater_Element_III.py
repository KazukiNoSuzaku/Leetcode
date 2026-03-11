# Given a positive integer n, find the smallest integer which has exactly the same digits
# existing in the integer n and is greater in value than n. Return -1 if no such positive integer exists.

# Author: Kaustav Ghosh

class Solution(object):
    def nextGreaterElement(self, n):
        digits = list(str(n))
        i = len(digits) - 2
        while i >= 0 and digits[i] >= digits[i+1]:
            i -= 1
        if i < 0: return -1
        j = len(digits) - 1
        while digits[j] <= digits[i]:
            j -= 1
        digits[i], digits[j] = digits[j], digits[i]
        digits[i+1:] = digits[i+1:][::-1]
        res = int(''.join(digits))
        return res if res <= 2**31 - 1 else -1
