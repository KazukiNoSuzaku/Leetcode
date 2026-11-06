# Author: Kaustav Ghosh
# Problem: Longest Substring Of All Vowels in Order
# Approach: A beautiful substring never goes backwards through the vowels, so scanning once and comparing each character with the one before it is enough: an equal character extends the current run, the next vowel in order extends it and marks one more vowel reached, and anything else breaks the run and restarts it. Tracking how many distinct vowels the current run has passed through means the all-five condition is a single comparison, so no substring is ever re-examined and the half-million character limit costs one pass.

class Solution(object):
    def longestBeautifulSubstring(self, word):
        """
        :type word: str
        :rtype: int
        """
        order = {"a": 0, "e": 1, "i": 2, "o": 3, "u": 4}
        best = 0
        length = 1
        reached = 1
        for previous, current in zip(word, word[1:]):
            if current == previous:
                length += 1
            elif order[current] == order[previous] + 1:
                length += 1
                reached += 1
            else:
                length = 1
                reached = 1
            if reached == 5 and length > best:
                best = length
        return best
