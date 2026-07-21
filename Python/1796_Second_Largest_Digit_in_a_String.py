# Author: Kaustav Ghosh
# Problem: Second Largest Digit in a String
# Approach: Collect the distinct digits present and return the second largest, or -1 if fewer than two exist

class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        digits = sorted({int(c) for c in s if c.isdigit()})
        return digits[-2] if len(digits) >= 2 else -1
