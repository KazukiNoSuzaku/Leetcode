# Author: Kaustav Ghosh
# Problem: Sum of Digits of String After Convert
# Approach: Replace each letter by its 1-indexed alphabet position and concatenate the digits, then repeat "replace by digit sum" k times

class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        num = ''.join(str(ord(c) - ord('a') + 1) for c in s)
        value = sum(int(d) for d in num)
        for _ in range(k - 1):
            value = sum(int(d) for d in str(value))
        return value
