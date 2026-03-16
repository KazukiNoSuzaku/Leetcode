# Author: Kaustav Ghosh
# Problem: String Matching in an Array
# Approach: Check each word as substring of any other word

class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        for i, w in enumerate(words):
            for j, other in enumerate(words):
                if i != j and w in other:
                    result.append(w)
                    break
        return result
