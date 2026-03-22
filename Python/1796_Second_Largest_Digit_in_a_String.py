# Author: Kaustav Ghosh

class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        digits = set()
        for c in s:
            if c.isdigit():
                digits.add(int(c))
        if len(digits) < 2:
            return -1
        digits.remove(max(digits))
        return max(digits)
