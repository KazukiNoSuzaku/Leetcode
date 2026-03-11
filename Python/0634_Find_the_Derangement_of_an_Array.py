# Count permutations of n elements where no element appears in its original position.
# Answer mod 10^9 + 7.

# Author: Kaustav Ghosh

class Solution(object):
    def findDerangement(self, n):
        MOD = 10**9 + 7
        if n == 0: return 1
        if n == 1: return 0
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, (i - 1) * (a + b) % MOD
        return b
