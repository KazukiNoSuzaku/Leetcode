# Author: Kaustav Ghosh
# Problem 1839: Longest Substring Of All Vowels in Order

class Solution(object):
    def longestBeautifulSubstring(self, word):
        """
        :type word: str
        :rtype: int
        """
        vowels = "aeiou"
        result = 0
        count = 1
        unique = 1
        for i in range(1, len(word)):
            if word[i] >= word[i - 1]:
                count += 1
                if word[i] != word[i - 1]:
                    unique += 1
            else:
                count = 1
                unique = 1
            if unique == 5:
                result = max(result, count)
        return result
