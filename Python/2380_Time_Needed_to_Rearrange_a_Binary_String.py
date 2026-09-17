# Author: Kaustav Ghosh
# Problem: Time Needed to Rearrange a Binary String
# Approach: Every second each "01" flips to "10", so a one slides left one zero per second unless the one ahead of it is in the way. Scanning left to right, a one preceded by z zeros lands at second max(previous one's finish + 1, z): it needs z seconds on its own but can never finish before the one ahead of it does

class Solution(object):
    def secondsToRemoveOccurrences(self, s):
        """
        :type s: str
        :rtype: int
        """
        zeros = 0
        seconds = 0
        for ch in s:
            if ch == '0':
                zeros += 1
            elif zeros:
                seconds = max(seconds + 1, zeros)
        return seconds
