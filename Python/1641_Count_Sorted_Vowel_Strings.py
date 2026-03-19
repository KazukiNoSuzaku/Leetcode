# Author: Kaustav Ghosh
# https://leetcode.com/problems/count-sorted-vowel-strings/

class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Stars and bars: C(n+4, 4)
        return (n + 1) * (n + 2) * (n + 3) * (n + 4) // 24
