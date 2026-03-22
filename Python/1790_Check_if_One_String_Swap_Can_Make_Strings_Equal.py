# Author: Kaustav Ghosh

class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        diffs = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diffs.append(i)
        if len(diffs) == 0:
            return True
        if len(diffs) == 2:
            return s1[diffs[0]] == s2[diffs[1]] and s1[diffs[1]] == s2[diffs[0]]
        return False
