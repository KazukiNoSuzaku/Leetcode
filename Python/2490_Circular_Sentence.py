# Author: Kaustav Ghosh
# Problem: Circular Sentence
# Approach: Split on the single spaces and check that each word's last letter matches the first letter of the next, wrapping the final word around to the first

class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        words = sentence.split()
        return all(word[-1] == words[(i + 1) % len(words)][0]
                   for i, word in enumerate(words))
