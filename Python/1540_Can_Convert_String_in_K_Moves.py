# Author: Kaustav Ghosh
# Problem: Can Convert String in K Moves
# Approach: Move number i may shift one character by i places, and each move index is usable once, so a character needing a shift of d can be served at move d, d + 26, d + 52 and so on. Count how many characters need each shift; the m-th of them must wait until move d + 26 * (m - 1), which has to stay within k. Unequal lengths make conversion impossible

from collections import Counter


class Solution(object):
    def canConvertString(self, s, t, k):
        """
        :type s: str
        :type t: str
        :type k: int
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        used = Counter()
        for a, b in zip(s, t):
            shift = (ord(b) - ord(a)) % 26
            if shift:
                used[shift] += 1
                if shift + 26 * (used[shift] - 1) > k:
                    return False
        return True
