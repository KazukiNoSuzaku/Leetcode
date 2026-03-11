# Skip all numbers containing digit 9. Find the n-th number in this sequence.

# Author: Kaustav Ghosh

class Solution(object):
    def newInteger(self, n):
        res = 0
        base = 1
        while n:
            res += (n % 9) * base
            n //= 9
            base *= 10
        return res
