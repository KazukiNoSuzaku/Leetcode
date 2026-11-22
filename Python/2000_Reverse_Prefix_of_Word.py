# Author: Kaustav Ghosh
# Problem: Reverse Prefix of Word
# Approach: Only the segment from the start of the word through the first occurrence of the given character moves, so the work is to locate that occurrence and splice the word back together with that segment reversed and the rest untouched. Searching for the character returns -1 when it never appears, which is exactly the case where the word is returned unchanged, so that check doubles as the guard. Both the search and the reversal are linear in the word's length.

class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        position = word.find(ch)
        if position == -1:
            return word
        return word[position::-1] + word[position + 1:]
