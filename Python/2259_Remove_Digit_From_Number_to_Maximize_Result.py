# Author: Kaustav Ghosh
# Problem: Remove Digit From Number to Maximize Result
# Approach: Try removing each occurrence of the target digit and keep the largest resulting number. Since the string length is fixed after removal, the largest string is the largest value

class Solution(object):
    def removeDigit(self, number, digit):
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        best = None
        for i, ch in enumerate(number):
            if ch == digit:
                candidate = number[:i] + number[i + 1:]
                if best is None or candidate > best:
                    best = candidate
        return best
