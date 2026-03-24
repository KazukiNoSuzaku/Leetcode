# Author: Kaustav Ghosh
# Problem 2062: Count Vowel Substrings of a String

class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        vowels = set('aeiou')
        count = 0
        n = len(word)
        for i in range(n):
            seen = set()
            for j in range(i, n):
                if word[j] not in vowels:
                    break
                seen.add(word[j])
                if len(seen) == 5:
                    count += 1
        return count
