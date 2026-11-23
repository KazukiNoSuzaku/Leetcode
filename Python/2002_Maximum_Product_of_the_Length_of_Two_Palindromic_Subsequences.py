# Author: Kaustav Ghosh
# Problem: Maximum Product of the Length of Two Palindromic Subsequences
# Approach: The string holds at most twelve characters, so every subset of positions can be examined directly: each subset is tested once for being a palindrome and its length recorded. Pairing every palindromic subset against every other would be quadratic in the number of subsets, so instead a subset-sum pass propagates, for each subset of positions, the longest palindrome available anywhere inside it, by taking the better of the subset itself and the subset with one position dropped. The answer is then the best product of a palindromic subset's length with the longest palindrome living in the positions it leaves free, which guarantees the two subsequences never share an index.

class Solution(object):
    def maxProduct(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = len(s)
        full = (1 << total) - 1
        palindrome = [0] * (full + 1)
        for mask in range(1, full + 1):
            chars = [s[index] for index in range(total) if mask >> index & 1]
            if chars == chars[::-1]:
                palindrome[mask] = len(chars)

        longest = palindrome[:]
        for bit in range(total):
            step = 1 << bit
            for mask in range(full + 1):
                if mask & step and longest[mask ^ step] > longest[mask]:
                    longest[mask] = longest[mask ^ step]

        answer = 0
        for mask in range(1, full + 1):
            if palindrome[mask]:
                product = palindrome[mask] * longest[full ^ mask]
                if product > answer:
                    answer = product
        return answer
