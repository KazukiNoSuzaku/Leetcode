# Author: Kaustav Ghosh
# Problem: Odd String Difference
# Approach: Reduce each word to its tuple of consecutive letter gaps and group the words by that tuple. All but one word share a tuple, so the group holding a single word names the odd one out

class Solution(object):
    def oddString(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        groups = {}
        for word in words:
            gaps = tuple(ord(b) - ord(a) for a, b in zip(word, word[1:]))
            groups.setdefault(gaps, []).append(word)
        return next(group[0] for group in groups.values() if len(group) == 1)
