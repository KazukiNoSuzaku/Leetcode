# Author: Kaustav Ghosh
# Problem: Second Largest Digit in a String
# Approach: Repeats of the same digit do not count as a second largest, so collecting the digits into a set first removes them, and sorting what remains puts the runner-up one place from the end. With fewer than two distinct digits there is no answer and -1 is returned.

class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        digits = sorted({int(c) for c in s if c.isdigit()})
        return digits[-2] if len(digits) > 1 else -1
