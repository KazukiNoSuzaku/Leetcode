# Author: Kaustav Ghosh
# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for c in set(s):
            first = s.index(c)
            last = s.rindex(c)
            if last > first:
                count += len(set(s[first + 1:last]))
        return count
