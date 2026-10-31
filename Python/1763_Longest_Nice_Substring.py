# Author: Kaustav Ghosh
# Problem: Longest Nice Substring
# Approach: If some letter appears in only one case inside the current window, no nice substring can contain that position, so the window splits there and the answer is the better of the two halves. Finding the first such offender and recursing on both sides therefore narrows the search quickly, and a window with no offender is itself nice and returned whole. Ties go to the left half so the earliest occurrence wins, matching the problem's tie-break.

class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return ""
        present = set(s)
        for index, letter in enumerate(s):
            if letter.swapcase() in present:
                continue
            left = self.longestNiceSubstring(s[:index])
            right = self.longestNiceSubstring(s[index + 1:])
            return right if len(right) > len(left) else left
        return s
