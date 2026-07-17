# Author: Kaustav Ghosh
# Problem: Longest Nice Substring
# Approach: Any character missing its opposite case can never be inside a nice substring, so split there and recurse on the two sides

class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return ''
        present = set(s)
        for i, c in enumerate(s):
            if c.swapcase() not in present:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i + 1:])
                return right if len(right) > len(left) else left
        return s
