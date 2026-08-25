# Author: Kaustav Ghosh
# Problem: Longest Palindrome by Concatenating Two Letter Words
# Approach: A word and its reverse can wrap around the palindrome, contributing 4 characters per matched pair. A symmetric word (like "gg") pairs with itself, and one leftover symmetric word can sit in the center adding 2

from collections import Counter

class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        count = Counter(words)
        length = 0
        has_center = False
        for w in count:
            r = w[::-1]
            if w == r:
                length += (count[w] // 2) * 4
                if count[w] % 2 == 1:
                    has_center = True
            elif w < r:
                length += min(count[w], count[r]) * 4
        if has_center:
            length += 2
        return length
