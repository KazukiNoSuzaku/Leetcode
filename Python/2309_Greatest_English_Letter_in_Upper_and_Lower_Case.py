# Author: Kaustav Ghosh
# Problem: Greatest English Letter in Upper and Lower Case
# Approach: Collect the set of characters, then scan letters from 'Z' down to 'A'; the first whose uppercase and lowercase forms both appear is the answer, returned in uppercase. If none qualify, return the empty string

class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        present = set(s)
        for code in range(ord('Z'), ord('A') - 1, -1):
            upper = chr(code)
            lower = chr(code + 32)
            if upper in present and lower in present:
                return upper
        return ""
