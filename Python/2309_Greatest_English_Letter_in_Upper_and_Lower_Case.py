# Author: Kaustav Ghosh
class Solution(object):
    def greatestLetter(self, s):
        # type: (str) -> str
        chars = set(s)
        for c in range(ord('Z'), ord('A') - 1, -1):
            if chr(c) in chars and chr(c + 32) in chars:
                return chr(c)
        return ""
