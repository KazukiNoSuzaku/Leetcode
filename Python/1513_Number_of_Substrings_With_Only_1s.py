# Author: Kaustav Ghosh
# Problem: Number of Substrings With Only 1s
# Approach: Each maximal run of ones of length L holds L * (L + 1) / 2 all-ones substrings, so track the current run and add its length at every '1', which accumulates exactly that total

class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        run = 0
        for ch in s:
            run = run + 1 if ch == '1' else 0
            total += run
        return total % (10 ** 9 + 7)
