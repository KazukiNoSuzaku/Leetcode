# Find probability that soup A runs out first or both run out at same time.

# Author: Kaustav Ghosh

class Solution(object):
    def soupServings(self, n):
        if n > 4800: return 1.0
        memo = {}
        def dp(a, b):
            if a <= 0 and b <= 0: return 0.5
            if a <= 0: return 1.0
            if b <= 0: return 0.0
            if (a, b) in memo: return memo[(a, b)]
            res = 0.25 * (dp(a-100,b) + dp(a-75,b-25) + dp(a-50,b-50) + dp(a-25,b-75))
            memo[(a, b)] = res
            return res
        return dp(n, n)
