# Author: Kaustav Ghosh
# Problem: Find Resultant Array After Removing Anagrams
# Approach: Repeatedly deleting a word that is an anagram of the one before it is equivalent to a single left-to-right pass that keeps a word only when its sorted letters differ from the last kept word's

class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        prev_key = None
        for w in words:
            key = "".join(sorted(w))
            if key != prev_key:
                result.append(w)
                prev_key = key
        return result
