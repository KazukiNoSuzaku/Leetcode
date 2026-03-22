# Author: Kaustav Ghosh

class Solution(object):
    def largestMerge(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = []
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            if word1[i:] >= word2[j:]:
                res.append(word1[i])
                i += 1
            else:
                res.append(word2[j])
                j += 1
        res.append(word1[i:])
        res.append(word2[j:])
        return ''.join(res)
