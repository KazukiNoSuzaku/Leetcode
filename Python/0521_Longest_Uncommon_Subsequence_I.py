# Given two strings a and b, return the length of the longest uncommon subsequence between them.
# If the longest uncommon subsequence doesn't exist, return -1.

# Author: Kaustav Ghosh

class Solution(object):
    def findLUSlength(self, a, b):
        return -1 if a == b else max(len(a), len(b))
