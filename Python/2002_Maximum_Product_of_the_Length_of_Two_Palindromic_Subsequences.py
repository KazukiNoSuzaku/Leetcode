# Author: Kaustav Ghosh
# Problem: Maximum Product of the Length of Two Palindromic Subsequences
# Approach: With n <= 12, enumerate every index subset and record its length if the chosen characters form a palindrome. Then for each palindromic subset, iterate submasks of its complement (disjoint) and maximize the product of lengths

class Solution(object):
    def maxProduct(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        full = (1 << n) - 1
        length = [0] * (1 << n)

        def is_pal(mask):
            chars = [s[i] for i in range(n) if mask >> i & 1]
            return chars == chars[::-1]

        for mask in range(1, 1 << n):
            if is_pal(mask):
                length[mask] = bin(mask).count('1')

        best = 0
        for mask in range(1, 1 << n):
            if length[mask] == 0:
                continue
            comp = full ^ mask
            sub = comp
            while sub > 0:
                if length[sub]:
                    best = max(best, length[mask] * length[sub])
                sub = (sub - 1) & comp
        return best
