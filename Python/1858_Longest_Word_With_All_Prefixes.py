# Author: Kaustav Ghosh
# Problem: Longest Word With All Prefixes
# Approach: A word qualifies exactly when the word one character shorter qualifies and is itself present, which turns the whole question into a chain that can be resolved shortest first. So the words are visited in order of length, and a word is admitted if it is a single character or if its own prefix was already admitted; no repeated prefix checking is needed and no trie has to be built. Sorting ties lexicographically means the first word admitted at any length is the smallest one, so taking only strictly longer words as the answer applies the required tie-break automatically.

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        qualified = set()
        best = ""
        for word in sorted(words, key=lambda w: (len(w), w)):
            if len(word) == 1 or word[:-1] in qualified:
                qualified.add(word)
                if len(word) > len(best):
                    best = word
        return best
