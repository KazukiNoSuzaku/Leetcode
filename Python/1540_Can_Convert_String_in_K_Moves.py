# Author: Kaustav Ghosh
# Problem: Can Convert String in K Moves
# Approach: For each position needing shift d, the j-th time we perform shift d costs d + 26*j moves; track next available move per shift

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
        count = [0] * 27
        for a, b in zip(s, t):
            diff = (ord(b) - ord(a)) % 26
            if diff != 0:
                count[diff] += 1
        for d in range(1, 27):
            if d + 26 * (count[d] - 1) > k:
                return False
        return True
