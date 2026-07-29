# Author: Kaustav Ghosh
# Problem: Substrings of Size Three with Distinct Characters
# Approach: Slide a length-3 window and count those whose three characters are all different

class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum(1 for i in range(len(s) - 2)
                   if s[i] != s[i + 1] and s[i + 1] != s[i + 2] and s[i] != s[i + 2])
