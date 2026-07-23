# Author: Kaustav Ghosh
# Problem: Truncate Sentence
# Approach: Split on spaces, keep the first k words, and rejoin

class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        return ' '.join(s.split()[:k])
