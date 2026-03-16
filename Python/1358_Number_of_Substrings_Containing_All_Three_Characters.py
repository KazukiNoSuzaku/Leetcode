# Author: Kaustav Ghosh
# Problem: Number of Substrings Containing All Three Characters
# Approach: Sliding window tracking last occurrence of a, b, c

class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        last = [-1, -1, -1]
        result = 0
        for i, c in enumerate(s):
            last[ord(c) - ord('a')] = i
            result += 1 + min(last)
        return result
