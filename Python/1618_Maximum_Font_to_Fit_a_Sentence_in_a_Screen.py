# Author: Kaustav Ghosh
# Problem: Maximum Font to Fit a Sentence in a Screen
# Approach: Characters only ever grow with the font size, so once a size fails to fit no larger one can, which makes the fonts array sorted by feasibility and the largest workable size a binary search away. The one thing worth care is the cost of a single feasibility test: the text may run to fifty thousand characters, so asking the interface for every character's width would make each test fifty thousand calls. Since the text is all lowercase letters, I tally the letters once and then a test needs at most twenty-six width queries weighted by those tallies, which keeps the whole run to a few hundred interface calls.

from collections import Counter


# """
# This is FontInfo's API interface.
# You should not implement it, or speculate about its implementation
# """
# class FontInfo(object):
#    Return the width of char ch when fontSize is used.
#    def getWidth(self, fontSize, ch):
#        """
#        :type fontSize: int
#        :type ch: char
#        :rtype int
#        """
#
#    def getHeight(self, fontSize):
#        """
#        :type fontSize: int
#        :rtype int
#        """


class Solution(object):
    def maxFont(self, text, w, h, fonts, fontInfo):
        """
        :type text: str
        :type w: int
        :type h: int
        :type fonts: List[int]
        :type fontInfo: FontInfo
        :rtype: int
        """
        tally = Counter(text).items()

        def fits(size):
            if fontInfo.getHeight(size) > h:
                return False
            total = 0
            for ch, times in tally:
                total += fontInfo.getWidth(size, ch) * times
                if total > w:
                    return False
            return True

        low, high = 0, len(fonts) - 1
        answer = -1
        while low <= high:
            middle = (low + high) // 2
            if fits(fonts[middle]):
                answer = fonts[middle]
                low = middle + 1
            else:
                high = middle - 1
        return answer
