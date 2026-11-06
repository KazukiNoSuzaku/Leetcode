# Author: Kaustav Ghosh
# Problem: Check if the Sentence Is Pangram
# Approach: The sentence is all lowercase letters, so collecting its characters into a set discards both the repeats and the ordering, and the only question left is whether all twenty-six letters survived. Comparing the set's size against twenty-six answers it in one pass without a per-letter scan.

class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        return len(set(sentence)) == 26
