# Author: Kaustav Ghosh
# Problem: Check if the Sentence Is Pangram
# Approach: A pangram uses all 26 letters, so the set of characters must have size 26

class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        return len(set(sentence)) == 26
