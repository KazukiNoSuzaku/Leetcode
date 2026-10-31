# Author: Kaustav Ghosh
# Problem: Merge Strings Alternately
# Approach: Zipping the two words pairs up letters only as far as the shorter one reaches, which is exactly the alternating part of the answer; whatever is left over belongs to the longer word and is appended unchanged. Slicing past the end of the shorter word yields an empty string, so the same expression handles both of which word is longer without a branch.

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        shared = min(len(word1), len(word2))
        merged = [letter for pair in zip(word1, word2) for letter in pair]
        return "".join(merged) + word1[shared:] + word2[shared:]
