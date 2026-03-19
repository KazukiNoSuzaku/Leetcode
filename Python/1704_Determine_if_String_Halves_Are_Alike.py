# Author: Kaustav Ghosh
# https://leetcode.com/problems/determine-if-string-halves-are-alike/

class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = set('aeiouAEIOU')
        mid = len(s) // 2
        return sum(c in vowels for c in s[:mid]) == sum(c in vowels for c in s[mid:])
