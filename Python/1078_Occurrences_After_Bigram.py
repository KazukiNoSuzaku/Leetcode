# Author: Kaustav Ghosh
# 1078. Occurrences After Bigram
# https://leetcode.com/problems/occurrences-after-bigram/

class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        words = text.split()
        result = []
        for i in range(len(words) - 2):
            if words[i] == first and words[i+1] == second:
                result.append(words[i+2])
        return result
