# Author: Kaustav Ghosh
# Problem: Number of Ways to Split a String
# Approach: Each part needs total_ones/3 ones; multiply the gap of zeros before the 2nd block by that before the 3rd. All-zeros is a C(n-1,2) special case

class Solution(object):
    def numWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        ones = [i for i, c in enumerate(s) if c == '1']
        total = len(ones)
        if total % 3:
            return 0
        n = len(s)
        if total == 0:
            return (n - 1) * (n - 2) // 2 % MOD
        k = total // 3
        way1 = ones[k] - ones[k - 1]
        way2 = ones[2 * k] - ones[2 * k - 1]
        return way1 * way2 % MOD
