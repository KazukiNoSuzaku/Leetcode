# Author: Kaustav Ghosh
# Problem: Vowels of All Substrings
# Approach: A vowel at index i belongs to (i+1)*(n-i) substrings (choices of left and right boundary). Sum that contribution over all vowels

class Solution(object):
    def countVowels(self, word):
        """
        :type word: str
        :rtype: int
        """
        vowels = set('aeiou')
        n = len(word)
        return sum((i + 1) * (n - i) for i, ch in enumerate(word) if ch in vowels)
