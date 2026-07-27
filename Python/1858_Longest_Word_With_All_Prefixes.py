# Author: Kaustav Ghosh
# Problem: Longest Word With All Prefixes (Premium)
# Approach: With all words in a set, a word qualifies when every proper prefix is also present; keep the longest, breaking ties by lexicographic order

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        present = set(words)
        best = ""
        for word in words:
            if all(word[:i] in present for i in range(1, len(word))):
                if len(word) > len(best) or (len(word) == len(best) and word < best):
                    best = word
        return best
