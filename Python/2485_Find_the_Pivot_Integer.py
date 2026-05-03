import math

class Solution:
    def pivotInteger(self, n: int) -> int:
        # sum(1..x) == sum(x..n) iff x^2 == n*(n+1)/2
        total = n * (n + 1) // 2
        x = math.isqrt(total)
        return x if x * x == total else -1
