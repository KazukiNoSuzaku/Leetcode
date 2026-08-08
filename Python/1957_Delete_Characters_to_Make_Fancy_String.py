# Author: Kaustav Ghosh
# Problem: Delete Characters to Make Fancy String
# Approach: Build the result greedily, appending each character unless the last two already equal it (which would create three in a row)

class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        out = []
        for ch in s:
            if len(out) >= 2 and out[-1] == ch and out[-2] == ch:
                continue
            out.append(ch)
        return ''.join(out)
