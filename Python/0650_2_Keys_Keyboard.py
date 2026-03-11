# Start with one 'A'. Each step: copy all or paste. Find min steps to get n 'A's.

# Author: Kaustav Ghosh

class Solution(object):
    def minSteps(self, n):
        res = 0
        d = 2
        while n > 1:
            while n % d == 0:
                res += d
                n //= d
            d += 1
        return res
