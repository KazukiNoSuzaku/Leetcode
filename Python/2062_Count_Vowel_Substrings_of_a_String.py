# Author: Kaustav Ghosh
# Problem: Count Vowel Substrings of a String
# Approach: A valid substring uses only vowels and contains all five. From each start, extend while characters stay vowels, tracking the distinct set; count each extension that holds all five vowels

class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        vowels = set('aeiou')
        n = len(word)
        count = 0
        for i in range(n):
            if word[i] not in vowels:
                continue
            seen = set()
            for j in range(i, n):
                if word[j] not in vowels:
                    break
                seen.add(word[j])
                if len(seen) == 5:
                    count += 1
        return count
