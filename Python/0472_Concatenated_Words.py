# Given an array of strings words (without duplicates), return all the concatenated words in the given list.
# A concatenated word is a string that is comprised entirely of at least two shorter words in the array.

# Author: Kaustav Ghosh

class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        word_set = set(words)

        def can_form(word):
            if not word:
                return False
            n = len(word)
            dp = [False] * (n + 1)
            dp[0] = True
            for i in range(1, n + 1):
                for j in range(i):
                    if dp[j] and word[j:i] in word_set and (j > 0 or i < n):
                        dp[i] = True
                        break
            return dp[n]

        return [w for w in words if can_form(w)]
