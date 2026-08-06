# Author: Kaustav Ghosh
# Problem: Check if String Is Decomposable Into Value-Equal Substrings
# Approach: Each maximal run of equal characters must be cut into pieces of size 3, with at most one size-2 piece overall. A run length L%3==1 is impossible; L%3==2 consumes the single allowed size-2 piece. Valid iff no run is %3==1 and exactly one run is %3==2

from itertools import groupby

class Solution(object):
    def isDecomposable(self, s):
        """
        :type s: str
        :rtype: bool
        """
        twos = 0
        for _, grp in groupby(s):
            length = len(list(grp))
            r = length % 3
            if r == 1:
                return False
            if r == 2:
                twos += 1
        return twos == 1
