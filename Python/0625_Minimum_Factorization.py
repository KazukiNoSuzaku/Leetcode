# Given a positive integer a, find the smallest number whose digits multiply to a.
# Return 0 if no such number exists.

# Author: Kaustav Ghosh

class Solution(object):
    def smallestFactorization(self, num):
        if num < 2: return num
        digits = []
        for d in range(9, 1, -1):
            while num % d == 0:
                digits.append(d)
                num //= d
        if num > 1: return 0
        res = int(''.join(map(str, digits[::-1])))
        return res if res < 2**31 else 0
