# Author: Kaustav Ghosh
# Problem: Check If a Word Occurs As a Prefix of Any Word in a Sentence
# Approach: Split sentence and check startswith

class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        for i, word in enumerate(sentence.split()):
            if word.startswith(searchWord):
                return i + 1
        return -1
