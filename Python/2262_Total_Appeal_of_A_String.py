# Author: Kaustav Ghosh
# Problem: Total Appeal of A String
# Approach: Each character contributes to a substring's appeal once, counted at its first occurrence within that substring. For position i holding a character last seen at index prev, it is the first such occurrence in substrings starting in (prev, i] and ending at or after i, giving (i - prev) * (n - i) contributions. Sum over all positions

class Solution(object):
    def appealSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        last = {}
        total = 0
        for i, ch in enumerate(s):
            prev = last.get(ch, -1)
            total += (i - prev) * (n - i)
            last[ch] = i
        return total
