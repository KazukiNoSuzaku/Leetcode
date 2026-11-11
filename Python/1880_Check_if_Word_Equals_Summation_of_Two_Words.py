# Author: Kaustav Ghosh
# Problem: Check if Word Equals Summation of Two Words
# Approach: Each letter from 'a' to 'j' stands for the digit of its position in the alphabet, so a word is read as a number by translating its letters and interpreting the result in base ten. Translating with a character map and letting int do the parsing also handles leading zeros the way the problem intends, since the numeric value is what gets compared.

class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        def value(word):
            return int("".join(str(ord(letter) - ord("a")) for letter in word))

        return value(firstWord) + value(secondWord) == value(targetWord)
