# Author: Kaustav Ghosh
# Problem: Count the Number of Consistent Strings
# Approach: A word qualifies when it introduces no character outside the allowed collection, which is exactly set containment, so turning the allowed characters into a set once makes each word a single subset test rather than a per-character scan against a string. The number of distinct characters in a word is at most twenty-six, so the test is effectively constant per word.

class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        permitted = set(allowed)
        return sum(1 for word in words if permitted.issuperset(word))
