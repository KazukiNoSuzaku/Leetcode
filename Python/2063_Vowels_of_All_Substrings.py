# Author: Kaustav Ghosh
# Problem 2063: Vowels of All Substrings

class Solution(object):
    def countVowels(self, word):
        """
        :type word: str
        :rtype: int
        """
        n = len(word)
        vowels = set('aeiou')
        total = 0
        for i in range(n):
            if word[i] in vowels:
                # This vowel appears in (i+1) * (n-i) substrings
                total += (i + 1) * (n - i)
        return total
