# Count integers in range [1, n] that have at least one repeated digit.

# Author: Kaustav Ghosh

class Solution(object):
    def numDupDigitsAtMostN(self, n):
        # Count numbers without repeated digits, subtract from n
        digits = list(map(int, str(n + 1)))
        k = len(digits)
        def perm(m, r):
            res = 1
            for i in range(r):
                res *= (m - i)
            return res
        # Count k-digit numbers without repeated digits strictly less
        count = 0
        seen = set()
        for i, d in enumerate(digits):
            # Place a digit < d at position i, rest can be any unused
            start = 1 if i == 0 else 0
            for x in range(start, d):
                if x not in seen:
                    count += perm(9 - i, k - i - 1)
            if d in seen:
                break
            seen.add(d)
            if i == k - 1:
                count += 1
        return n - count
