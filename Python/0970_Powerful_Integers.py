# Return all powerful integers: x^i + y^j <= bound for i,j >= 0.

# Author: Kaustav Ghosh

class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        res = set()
        xi = 1
        while xi < bound:
            yj = 1
            while xi + yj <= bound:
                res.add(xi + yj)
                if y == 1: break
                yj *= y
            if x == 1: break
            xi *= x
        return list(res)
