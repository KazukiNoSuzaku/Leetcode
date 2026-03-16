# Author: Kaustav Ghosh
# Problem: Consecutive Characters
# Approach: Track max run of same character

class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_run = 1
        run = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                run += 1
                max_run = max(max_run, run)
            else:
                run = 1
        return max_run
