# Author: Kaustav Ghosh
# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        return max(len(s.split()) for s in sentences)
