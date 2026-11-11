# Author: Kaustav Ghosh
# Problem: Substrings of Size Three with Distinct Characters
# Approach: Every window of three consecutive characters is examined once, and three characters are all different exactly when putting them in a set leaves three entries, which is cheaper to state than comparing the three pairs by hand. The windows are taken by slicing, so nothing needs to be carried between steps.

class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum(1 for start in range(len(s) - 2) if len(set(s[start:start + 3])) == 3)
