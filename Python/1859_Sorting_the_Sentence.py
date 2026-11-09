# Author: Kaustav Ghosh
# Problem: Sorting the Sentence
# Approach: Each shuffled token carries its own destination as its final character, and the sentence has at most nine words, so the position is a single digit read straight off the end. Placing every word directly into a slot of the right size avoids sorting altogether, and the trailing digit is dropped by slicing before the pieces are joined with single spaces.

class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        tokens = s.split()
        ordered = [""] * len(tokens)
        for token in tokens:
            ordered[int(token[-1]) - 1] = token[:-1]
        return " ".join(ordered)
