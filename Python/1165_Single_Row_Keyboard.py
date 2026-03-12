# Premium problem - not available without subscription
# Author: Kaustav Ghosh
# Typical approach: Sum distances between consecutive characters on keyboard

class Solution(object):
    def calculateTime(self, keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """
        pos = {c: i for i, c in enumerate(keyboard)}
        result = 0
        prev = 0
        for c in word:
            result += abs(pos[c] - prev)
            prev = pos[c]
        return result
