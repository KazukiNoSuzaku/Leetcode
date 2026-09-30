# Author: Kaustav Ghosh
# Problem: Count Palindromic Subsequences
# Approach: A palindrome of length five looks like a b m b a, so fix the middle position and multiply the number of "ab" pairs before it by the number of "ba" pairs after it, summed over the 100 digit combinations. Two sweeps record, for every position, how many two-digit subsequences of each kind lie on each side

class Solution(object):
    def countPalindromes(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        n = len(s)

        before = [None] * n
        single = [0] * 10
        pairs = [[0] * 10 for _ in range(10)]
        for i, ch in enumerate(s):
            before[i] = [row[:] for row in pairs]
            digit = int(ch)
            for first in range(10):
                pairs[first][digit] += single[first]
            single[digit] += 1

        after = [None] * n
        single = [0] * 10
        pairs = [[0] * 10 for _ in range(10)]
        for i in range(n - 1, -1, -1):
            after[i] = [row[:] for row in pairs]
            digit = int(s[i])
            for second in range(10):
                pairs[digit][second] += single[second]
            single[digit] += 1

        total = 0
        for i in range(n):
            left, right = before[i], after[i]
            for a in range(10):
                for b in range(10):
                    total += left[a][b] * right[b][a]
        return total % MOD
