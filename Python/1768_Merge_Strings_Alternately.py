# Author: Kaustav Ghosh

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = []
        i = 0
        while i < len(word1) and i < len(word2):
            res.append(word1[i])
            res.append(word2[i])
            i += 1
        res.append(word1[i:])
        res.append(word2[i:])
        return ''.join(res)
