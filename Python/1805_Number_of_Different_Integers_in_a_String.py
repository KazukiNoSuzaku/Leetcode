# Author: Kaustav Ghosh
# Problem: Number of Different Integers in a String
# Approach: Replace every letter with a space to split out the number runs, then count distinct values (int() drops leading zeros)

class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        cleaned = ''.join(c if c.isdigit() else ' ' for c in word)
        return len({int(tok) for tok in cleaned.split()})
