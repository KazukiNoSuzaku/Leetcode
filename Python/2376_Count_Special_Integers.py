from math import perm

class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        digits = list(map(int, str(n)))
        k = len(digits)
        result = 0
        used = set()

        # Count all special numbers with fewer than k digits
        for length in range(1, k):
            result += 9 * perm(9, length - 1)

        # Count k-digit special numbers <= n using digit DP
        for i, d in enumerate(digits):
            start = 1 if i == 0 else 0
            for x in range(start, d):
                if x not in used:
                    result += perm(9 - i, k - i - 1)
            if d in used:
                break
            used.add(d)
        else:
            result += 1  # n itself is special

        return result
