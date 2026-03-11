# Given two non-negative integers, num1 and num2 represented as string,
# return the sum of num1 and num2 as a string.
# You must solve the problem without using any built-in library for big integers.

# Author: Kaustav Ghosh

class Solution(object):
    def addStrings(self, num1, num2):
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        res = []
        while i >= 0 or j >= 0 or carry:
            a = ord(num1[i]) - ord('0') if i >= 0 else 0
            b = ord(num2[j]) - ord('0') if j >= 0 else 0
            total = a + b + carry
            res.append(str(total % 10))
            carry = total // 10
            i -= 1
            j -= 1
        return ''.join(reversed(res))
