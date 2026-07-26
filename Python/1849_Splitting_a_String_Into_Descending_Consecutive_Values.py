# Author: Kaustav Ghosh
# Problem: Splitting a String Into Descending Consecutive Values
# Approach: Backtrack the first cut to fix the leading value, then require every following chunk to equal the previous value minus one; leading zeros are fine since int() parses them

class Solution(object):
    def splitString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)

        def backtrack(start, prev):
            if start == n:
                return True
            for end in range(start + 1, n + 1):
                value = int(s[start:end])
                if value == prev - 1 and backtrack(end, value):
                    return True
                if value > prev - 1:  # chunk already too big, longer only grows
                    break
            return False

        # First chunk sets the initial value; it must leave at least one more chunk
        for end in range(1, n):
            first = int(s[:end])
            if backtrack(end, first):
                return True
        return False
