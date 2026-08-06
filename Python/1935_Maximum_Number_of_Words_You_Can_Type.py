# Author: Kaustav Ghosh
# Problem: Maximum Number of Words You Can Type
# Approach: A word is typeable if none of its letters are broken. Count words whose character set is disjoint from the set of broken letters

class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        broken = set(brokenLetters)
        return sum(1 for word in text.split() if not (set(word) & broken))
