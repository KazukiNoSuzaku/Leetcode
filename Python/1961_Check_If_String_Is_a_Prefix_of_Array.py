# Author: Kaustav Ghosh
# Problem: Check If String Is a Prefix of Array
# Approach: s has to be the concatenation of the first k words for some k, so there is no choice to make: the words must be consumed in order and each one must match the next stretch of s exactly. I walk the words keeping how much of s has been matched, compare each word against the slice of s starting there, and fail the moment a word disagrees or runs past the end of s. Success is reaching exactly the end of s at a word boundary, which is why the loop returns true only when the matched length equals the length of s and returns false if the words run out first. That is one pass over the shorter of the two, so O(len(s)) time.

class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        matched = 0
        for word in words:
            if s[matched:matched + len(word)] != word:
                return False
            matched += len(word)
            if matched == len(s):
                return True
        return False
