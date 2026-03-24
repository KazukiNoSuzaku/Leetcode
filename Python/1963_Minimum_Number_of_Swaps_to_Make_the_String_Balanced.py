# Author: Kaustav Ghosh
# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/

class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Count max unmatched closing brackets
        unmatched = 0
        max_unmatched = 0
        for c in s:
            if c == '[':
                unmatched -= 1
            else:
                unmatched += 1
            max_unmatched = max(max_unmatched, unmatched)
        return (max_unmatched + 1) // 2
