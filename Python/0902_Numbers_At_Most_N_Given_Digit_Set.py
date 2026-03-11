# Count numbers <= n formed from given sorted digits.

# Author: Kaustav Ghosh

class Solution(object):
    def atMostNGivenDigitSet(self, digits, n):
        s = str(n)
        k = len(s)
        d = len(digits)
        res = sum(d**i for i in range(1, k))
        for i, c in enumerate(s):
            lt = sum(1 for dig in digits if dig < c)
            res += lt * (d ** (k - 1 - i))
            if c not in digits: break
            if i == k - 1: res += 1
        return res
