# Given an array of strings wordsDict and two different strings word1 and word2,
# return the shortest distance between these two words in the list.

# Example 1:
# Input: wordsDict = ["practice","makes","perfect","coding","makes"], word1 = "coding", word2 = "practice"
# Output: 3

# Example 2:
# Input: wordsDict = ["practice","makes","perfect","coding","makes"], word1 = "makes", word2 = "coding"
# Output: 1

# Constraints:
# 2 <= wordsDict.length <= 3 * 10^4
# 1 <= wordsDict[i].length <= 10

# Author: Kaustav Ghosh

class Solution(object):
    def shortestDistance(self, wordsDict, word1, word2):
        i1 = i2 = -1
        res = float('inf')
        for i, w in enumerate(wordsDict):
            if w == word1:
                i1 = i
            elif w == word2:
                i2 = i
            if i1 != -1 and i2 != -1:
                res = min(res, abs(i1 - i2))
        return res
