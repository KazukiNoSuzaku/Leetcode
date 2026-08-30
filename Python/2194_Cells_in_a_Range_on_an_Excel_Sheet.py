# Author: Kaustav Ghosh
# Problem: Cells in a Range on an Excel Sheet
# Approach: Parse the two corner cells (column letter + row number). Enumerate cells column by column, and within each column by row, matching the required ordering

class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        c1, r1, c2, r2 = s[0], int(s[1]), s[3], int(s[4])
        result = []
        for col in range(ord(c1), ord(c2) + 1):
            for row in range(r1, r2 + 1):
                result.append(chr(col) + str(row))
        return result
