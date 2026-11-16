# Author: Kaustav Ghosh
# Problem: Check if String Is Decomposable Into Value-Equal Substrings
# Approach: Every piece of the decomposition is value-equal, so no piece can straddle the boundary between two maximal runs of identical digits; each run must therefore be cut up on its own into threes plus at most the single allowed two. A run of length L can be split into threes exactly when L is divisible by three, can be split into threes and one two when L leaves remainder two, and can never be split when it leaves remainder one. So I walk the runs with two pointers, reject immediately on remainder one, tally how many runs need the length-two piece, and reject a second such run; the string decomposes precisely when exactly one run claimed it.

class Solution(object):
    def isDecomposable(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        twos = 0
        start = 0
        while start < length:
            end = start
            while end < length and s[end] == s[start]:
                end += 1
            leftover = (end - start) % 3
            if leftover == 1:
                return False
            if leftover == 2:
                twos += 1
                if twos > 1:
                    return False
            start = end
        return twos == 1
