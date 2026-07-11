# Author: Kaustav Ghosh
# Problem: Count the Number of Consistent Strings
# Approach: A word is consistent when its character set is a subset of the allowed set; count those

class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        allowed_set = set(allowed)
        return sum(1 for word in words if set(word) <= allowed_set)
