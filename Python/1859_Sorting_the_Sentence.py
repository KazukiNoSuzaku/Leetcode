# Author: Kaustav Ghosh
# Problem: Sorting the Sentence
# Approach: Each token ends with its 1-based position, so place its letters into that slot and join

class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        result = [''] * len(words)
        for token in words:
            result[int(token[-1]) - 1] = token[:-1]
        return ' '.join(result)
