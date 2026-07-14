# Author: Kaustav Ghosh
# Problem: Change Minimum Characters to Satisfy One of Three Conditions
# Approach: Try all 26 letters for the "both strings are one letter" case, and all 25 split points for the two ordering cases (everything in one string below the split, everything in the other at or above)

from collections import Counter

class Solution(object):
    def minCharacters(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        ca, cb = Counter(a), Counter(b)
        m, n = len(a), len(b)
        best = float('inf')

        # Condition 3: both strings become a single repeated letter
        for i in range(26):
            c = chr(97 + i)
            best = min(best, (m - ca[c]) + (n - cb[c]))

        # Conditions 1 and 2: split at letter c, one side strictly below it
        for i in range(1, 26):
            a_high = sum(ca[chr(97 + j)] for j in range(i, 26))
            a_low = sum(ca[chr(97 + j)] for j in range(i))
            b_high = sum(cb[chr(97 + j)] for j in range(i, 26))
            b_low = sum(cb[chr(97 + j)] for j in range(i))
            best = min(best, a_high + b_low, b_high + a_low)

        return best
