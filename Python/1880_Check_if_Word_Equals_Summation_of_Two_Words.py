# Author: Kaustav Ghosh
# Problem: Check if Word Equals Summation of Two Words
# Approach: Map each letter a..j to a digit 0..9 to read each word as a number, then check the first two sum to the target

class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        def value(word):
            return int(''.join(str(ord(c) - 97) for c in word))

        return value(firstWord) + value(secondWord) == value(targetWord)
