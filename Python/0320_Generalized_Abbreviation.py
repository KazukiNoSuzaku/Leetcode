# A word's generalized abbreviation can be constructed by taking any number of non-overlapping
# and non-adjacent substrings and replacing them with their respective lengths.
# Given a string word, return a list of all possible generalized abbreviations of word.

# Example 1:
# Input: word = "word"
# Output: ["4","3d","2r1","2rd","1o2","1o1d","1or1","1ord","w3","w2d","w1r1","w1rd","wo2","wo1d","wor1","word"]

# Example 2:
# Input: word = "a"
# Output: ["1","a"]

# Constraints:
# 1 <= word.length <= 15

# Author: Kaustav Ghosh

class Solution(object):
    def generateAbbreviations(self, word):
        res = []
        def dfs(pos, cur, count):
            if pos == len(word):
                res.append(cur + (str(count) if count > 0 else ''))
                return
            dfs(pos + 1, cur, count + 1)
            dfs(pos + 1, cur + (str(count) if count > 0 else '') + word[pos], 0)
        dfs(0, '', 0)
        return res
