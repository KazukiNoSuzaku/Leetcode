from math import gcd

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        g = gcd(a, b)
        return sum(1 for i in range(1, g + 1) if g % i == 0)
