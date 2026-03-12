# Author: Kaustav Ghosh
# 1119. Remove Vowels from a String
# https://leetcode.com/problems/remove-vowels-from-a-string/

class Solution(object):
    def removeVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set('aeiou')
        return ''.join(c for c in s if c not in vowels)
