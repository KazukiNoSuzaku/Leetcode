# Author: Kaustav Ghosh
# https://leetcode.com/problems/maximum-number-of-words-you-can-type/

class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        broken = set(brokenLetters)
        count = 0
        for word in text.split():
            if not any(c in broken for c in word):
                count += 1
        return count
