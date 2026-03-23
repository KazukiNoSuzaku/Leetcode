# Author: Kaustav Ghosh
# Problem 1858: Longest Word With All Prefixes (Premium)

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        word_set = set(words)
        result = ""
        for word in words:
            valid = True
            for i in range(1, len(word)):
                if word[:i] not in word_set:
                    valid = False
                    break
            if valid:
                if len(word) > len(result) or (len(word) == len(result) and word < result):
                    result = word
        return result
