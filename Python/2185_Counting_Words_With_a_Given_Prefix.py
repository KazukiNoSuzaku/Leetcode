# Author: Kaustav Ghosh
# Problem: Counting Words With a Given Prefix
# Approach: Count how many words start with the given prefix using string startswith

class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        return sum(1 for w in words if w.startswith(pref))
