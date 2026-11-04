# Author: Kaustav Ghosh
# Problem: Truncate Sentence
# Approach: The sentence has single spaces and no padding, so splitting it yields exactly its words, and keeping the first k of them and rejoining with single spaces rebuilds the truncated sentence unchanged.

class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        return " ".join(s.split()[:k])
