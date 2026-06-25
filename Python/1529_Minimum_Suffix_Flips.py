# Author: Kaustav Ghosh
# Problem: Minimum Suffix Flips
# Approach: Count transitions in target from the implicit '0' start; each change in value requires one flip

class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        ans = 0
        current = '0'
        for c in target:
            if c != current:
                ans += 1
                current = c
        return ans
