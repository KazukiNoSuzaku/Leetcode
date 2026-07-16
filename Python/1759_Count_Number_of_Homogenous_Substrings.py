# Author: Kaustav Ghosh
# Problem: Count Number of Homogenous Substrings
# Approach: A position inside a run of length L ends exactly L homogenous substrings, so track the run length and add it each step (summing to L*(L+1)/2 per run)

class Solution(object):
    def countHomogenous(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        total = 0
        run = 0
        prev = ''
        for c in s:
            run = run + 1 if c == prev else 1
            prev = c
            total += run
        return total % MOD
