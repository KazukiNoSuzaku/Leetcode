# Author: Kaustav Ghosh
# Problem: Check if One String Swap Can Make Strings Equal
# Approach: A single swap can only repair the positions where the strings disagree, and it touches exactly two of them, so the strings can match only if they already agree everywhere or disagree in precisely two places. In the latter case the swap has to put each mismatched character where the other one is, which means the two disagreeing pairs must be mirror images of each other.

class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        mismatches = [(a, b) for a, b in zip(s1, s2) if a != b]
        if not mismatches:
            return True
        return len(mismatches) == 2 and mismatches[0] == mismatches[1][::-1]
