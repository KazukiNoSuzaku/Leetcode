# Author: Kaustav Ghosh
# Problem: 1540 - Can Convert String in K Moves
# Approach: Count shift frequencies, check each fits within k moves

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

        count = [0] * 26
        for sc, tc in zip(s, t):
            diff = (ord(tc) - ord(sc)) % 26
            if diff != 0:
                count[diff] += 1

        for shift in range(1, 26):
            needed = shift + 26 * (count[shift] - 1)
            if count[shift] > 0 and needed > k:
                return False

        return True
