class Solution:
    def minOperations(self, n: int) -> int:
        # Non-adjacent form: single 1-bit costs 1 op; two consecutive 1s, round up (carry) and count 1 op.
        ops = 0
        while n:
            if n & 1:
                if n & 3 == 3:
                    n += 1
                else:
                    n -= 1
                ops += 1
            n >>= 1
        return ops
