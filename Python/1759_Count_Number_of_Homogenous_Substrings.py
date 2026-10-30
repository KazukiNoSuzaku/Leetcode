# Author: Kaustav Ghosh
# Problem: Count Number of Homogenous Substrings
# Approach: A homogenous substring lies entirely within one run of equal characters, and the runs are independent, so the count is the sum over runs of how many substrings each contains, which for a run of length L is L(L+1)/2. Walking the string once and tracking the current run's length gives every run without storing them, and the modulus is applied at the end since the total is the only quantity that can grow large.

class Solution(object):
    def countHomogenous(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        total = 0
        run = 0
        previous = ''
        for ch in s:
            run = run + 1 if ch == previous else 1
            previous = ch
            total += run
        return total % MOD
