# An additive number is a string whose digits can form an additive sequence.
# A valid additive sequence should contain at least three numbers. Except for the first two numbers,
# each subsequent number in the sequence must equal the sum of the preceding two.
# Given a string num, return true if it is an additive number or false otherwise.

# Example 1:
# Input: num = "112358"
# Output: true

# Example 2:
# Input: num = "199100199"
# Output: true

# Constraints:
# 1 <= num.length <= 35
# num consists only of digits.

# Author: Kaustav Ghosh

class Solution(object):
    def isAdditiveNumber(self, num):
        n = len(num)
        for i in range(1, n):
            for j in range(i + 1, n):
                a, b = num[:i], num[i:j]
                if (len(a) > 1 and a[0] == '0') or (len(b) > 1 and b[0] == '0'):
                    continue
                a, b = int(a), int(b)
                pos = j
                while pos < n:
                    c = a + b
                    sc = str(c)
                    if not num[pos:].startswith(sc):
                        break
                    pos += len(sc)
                    a, b = b, c
                if pos == n:
                    return True
        return False
