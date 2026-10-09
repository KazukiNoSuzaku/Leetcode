# Author: Kaustav Ghosh
# Problem: Make The String Great
# Approach: Removing a bad pair can only expose one new neighbouring pair, which is exactly what a stack handles: push each character, but if it is the case-flipped twin of the top, pop instead. What remains has no bad pair anywhere

class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        kept = []
        for ch in s:
            if kept and kept[-1] != ch and kept[-1].lower() == ch.lower():
                kept.pop()
            else:
                kept.append(ch)
        return "".join(kept)
