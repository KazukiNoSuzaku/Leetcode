# Author: Kaustav Ghosh
# Problem: Length of the Longest Alphabetical Continuous Substring
# Approach: Walk the string tracking the length of the run ending at the current letter, extending it while each letter is the alphabetical successor of the previous one and resetting to 1 otherwise

class Solution(object):
    def longestContinuousSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        best = run = 1
        for i in range(1, len(s)):
            run = run + 1 if ord(s[i]) - ord(s[i - 1]) == 1 else 1
            best = max(best, run)
        return best
