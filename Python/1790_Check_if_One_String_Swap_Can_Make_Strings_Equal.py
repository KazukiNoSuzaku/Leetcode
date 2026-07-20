# Author: Kaustav Ghosh
# Problem: Check if One String Swap Can Make Strings Equal
# Approach: Collect the mismatched positions; they are fixable iff there are none (already equal) or exactly two that are mirror images

class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        diffs = [(a, b) for a, b in zip(s1, s2) if a != b]
        if not diffs:
            return True
        return len(diffs) == 2 and diffs[0] == diffs[1][::-1]
