# Author: Kaustav Ghosh
# 2315. Count Asterisks
# Count '*' characters that appear between pairs of '|' (outside pipes ignored)

class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        inside = False

        for c in s:
            if c == '|':
                inside = not inside
            elif c == '*' and not inside:
                count += 1

        return count
