# Author: Kaustav Ghosh
# Problem: Determine if String Halves Are Alike
# Approach: Count vowels in each half and compare

class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = set('aeiouAEIOU')
        half = len(s) // 2
        first = sum(c in vowels for c in s[:half])
        second = sum(c in vowels for c in s[half:])
        return first == second
