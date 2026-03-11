# Given an array of strings words, return true if it forms a valid word square.
# A sequence of strings forms a valid word square if the kth row and column read the same string.

# Author: Kaustav Ghosh

class Solution(object):
    def validWordSquare(self, words):
        for i, row in enumerate(words):
            for j, ch in enumerate(row):
                if j >= len(words) or i >= len(words[j]) or words[j][i] != ch:
                    return False
        return True
