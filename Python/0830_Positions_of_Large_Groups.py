# Find start and end indices of groups of 3+ identical consecutive characters.

# Author: Kaustav Ghosh

class Solution(object):
    def largeGroupPositions(self, s):
        res = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]: j += 1
            if j - i >= 3: res.append([i, j - 1])
            i = j
        return res
