# Author: Kaustav Ghosh
# Problem 2002: Maximum Product of the Length of Two Palindromic Subsequences

class Solution(object):
    def maxProduct(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        # Precompute palindrome length for each bitmask
        def is_palindrome(mask):
            chars = []
            for i in range(n):
                if mask & (1 << i):
                    chars.append(s[i])
            return chars == chars[::-1]

        pal_len = {}
        for mask in range(1, 1 << n):
            if is_palindrome(mask):
                pal_len[mask] = bin(mask).count('1')

        full = (1 << n) - 1
        result = 0
        for m1, l1 in pal_len.items():
            complement = full ^ m1
            sub = complement
            while sub > 0:
                if sub in pal_len:
                    result = max(result, l1 * pal_len[sub])
                sub = (sub - 1) & complement
        return result
