# Count lines and last line width when writing a string with given widths.

# Author: Kaustav Ghosh

class Solution(object):
    def numberOfLines(self, widths, s):
        lines, cur = 1, 0
        for c in s:
            w = widths[ord(c) - ord('a')]
            if cur + w > 100:
                lines += 1; cur = 0
            cur += w
        return [lines, cur]
