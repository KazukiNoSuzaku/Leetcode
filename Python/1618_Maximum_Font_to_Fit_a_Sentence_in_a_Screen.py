# Author: Kaustav Ghosh
# Problem: Maximum Font to Fit a Sentence in a Screen (Premium)
# Approach: "fits" is monotonic in font size, so binary search the sorted fonts for the largest one whose total width and height stay within the screen

# """
# This is FontInfo's API interface.
# class FontInfo(object):
#    def getWidth(self, fontSize, ch):
#        :type fontSize: int
#        :type ch: char
#        :rtype int
#    def getHeight(self, fontSize):
#        :type fontSize: int
#        :rtype int
# """

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
        def fits(size):
            if fontInfo.getHeight(size) > h:
                return False
            total = sum(fontInfo.getWidth(size, ch) for ch in text)
            return total <= w

        lo, hi = 0, len(fonts) - 1
        best = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if fits(fonts[mid]):
                best = fonts[mid]
                lo = mid + 1
            else:
                hi = mid - 1
        return best
