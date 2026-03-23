# Author: Kaustav Ghosh
# Problem 1832: Check if the Sentence Is Pangram

class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        return len(set(sentence)) == 26
