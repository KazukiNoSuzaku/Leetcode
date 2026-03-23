# Author: Kaustav Ghosh
# Problem 1880: Check if Word Equals Summation of Two Words

class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        def word_value(word):
            val = 0
            for c in word:
                val = val * 10 + (ord(c) - ord('a'))
            return val

        return word_value(firstWord) + word_value(secondWord) == word_value(targetWord)
