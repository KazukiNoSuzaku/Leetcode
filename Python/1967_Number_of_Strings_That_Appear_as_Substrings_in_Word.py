# Author: Kaustav Ghosh
# Problem: Number of Strings That Appear as Substrings in Word
# Approach: Each pattern is tested on its own and repeated patterns each count separately, so there is nothing to deduplicate and the answer is simply how many entries of the list occur inside word. Python's substring operator does the containment test, and with word at most a hundred characters and a hundred patterns of at most a hundred characters each the total work is tiny, so a direct scan per pattern is the right trade rather than building an index over word.

class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        return sum(1 for pattern in patterns if pattern in word)
