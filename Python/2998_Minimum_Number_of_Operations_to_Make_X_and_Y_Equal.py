from functools import lru_cache

class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        @lru_cache(maxsize=None)
        def dp(n: int) -> int:
            if n <= y:
                return y - n  # only increments needed
            # Option 1: decrement/increment to y directly
            res = n - y
            # Option 2: subtract to nearest multiple of 11, then divide
            res = min(res, n % 11 + 1 + dp(n // 11))
            # Option 3: add to nearest multiple of 11, then divide
            if n % 11:
                res = min(res, (11 - n % 11) + 1 + dp(n // 11 + 1))
            # Option 4: subtract to nearest multiple of 5, then divide
            res = min(res, n % 5 + 1 + dp(n // 5))
            # Option 5: add to nearest multiple of 5, then divide
            if n % 5:
                res = min(res, (5 - n % 5) + 1 + dp(n // 5 + 1))
            return res

        return dp(x)
