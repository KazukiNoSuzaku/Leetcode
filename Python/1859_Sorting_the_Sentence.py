# Author: Kaustav Ghosh
# Problem 1859: Sorting the Sentence

class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        result = [""] * len(words)
        for word in words:
            idx = int(word[-1]) - 1
            result[idx] = word[:-1]
        return " ".join(result)
