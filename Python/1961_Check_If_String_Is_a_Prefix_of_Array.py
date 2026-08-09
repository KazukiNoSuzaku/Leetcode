# Author: Kaustav Ghosh
# Problem: Check If String Is a Prefix of Array
# Approach: Concatenate words one by one, checking that each stays a prefix of s. Succeed the moment the built string equals s; fail if a word diverges or we run out

class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        built = ""
        for w in words:
            built += w
            if built == s:
                return True
            if not s.startswith(built):
                return False
        return False
