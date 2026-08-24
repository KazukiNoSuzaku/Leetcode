# Author: Kaustav Ghosh
# Problem: Maximum Number of Words Found in Sentences
# Approach: The number of words in a sentence is its space count plus one; return the maximum across all sentences

class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        return max(s.count(' ') + 1 for s in sentences)
