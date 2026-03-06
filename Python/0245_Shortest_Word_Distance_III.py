# Given an array of strings wordsDict and two strings word1 and word2, return the shortest
# distance between these two words in the list.
# Note that word1 and word2 may be the same. They should be considered two distinct words.

# Example 1:
# Input: wordsDict = ["practice","makes","perfect","coding","makes"], word1 = "makes", word2 = "coding"
# Output: 1

# Example 2:
# Input: wordsDict = ["practice","makes","perfect","coding","makes"], word1 = "makes", word2 = "makes"
# Output: 3

# Constraints:
# 2 <= wordsDict.length <= 10^5

# Author: Kaustav Ghosh

class Solution(object):
    def shortestWordDistance(self, wordsDict, word1, word2):
        i1 = i2 = -1
        res = float('inf')
        same = (word1 == word2)
        for i, w in enumerate(wordsDict):
            if w == word1:
                if same:
                    if i1 != -1:
                        res = min(res, i - i1)
                    i1 = i
                else:
                    i1 = i
            elif w == word2:
                i2 = i
            if not same and i1 != -1 and i2 != -1:
                res = min(res, abs(i1 - i2))
        return res
