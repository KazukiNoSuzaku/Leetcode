# Author: Kaustav Ghosh
# Problem: Check if Number Has Equal Digit Count and Digit Value
# Approach: Count how many times each digit appears, then verify that for every index i the digit at position i equals the number of occurrences of the digit i in the string

from collections import Counter


class Solution(object):
    def digitCount(self, num):
        """
        :type num: str
        :rtype: bool
        """
        counts = Counter(num)
        for i, ch in enumerate(num):
            if counts[str(i)] != int(ch):
                return False
        return True
