# Author: Kaustav Ghosh
# Problem: Splitting a String Into Descending Consecutive Values
# Approach: Once the first piece is fixed every later piece is forced, because each must be exactly one less than the one before it, so the only real choice is where the first cut goes. Trying each of those cuts and then following the forced chain is therefore enough, and the chain is cheap to walk: a candidate piece is extended digit by digit and abandoned as soon as its value passes the required one, which it does quickly since the value only grows. Leading zeros need no special handling because a piece is compared by its numeric value, and the first piece is never allowed to swallow the whole string so at least two pieces always remain.

class Solution(object):
    def splitString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)

        def follows(start, previous):
            if start == n:
                return True
            if previous == 0:
                return False
            value = 0
            for end in range(start, n):
                value = value * 10 + int(s[end])
                if value > previous - 1:
                    break
                if value == previous - 1 and follows(end + 1, value):
                    return True
            return False

        first = 0
        for end in range(n - 1):
            first = first * 10 + int(s[end])
            if follows(end + 1, first):
                return True
        return False
