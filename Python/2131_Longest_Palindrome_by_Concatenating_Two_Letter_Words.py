# Author: Kaustav Ghosh
# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

from collections import Counter

class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        count = Counter(words)
        result = 0
        has_center = False

        for word in list(count.keys()):
            rev = word[::-1]
            if word == rev:
                pairs = count[word] // 2
                result += pairs * 4
                if count[word] % 2 == 1:
                    has_center = True
            elif word < rev and rev in count:
                pairs = min(count[word], count[rev])
                result += pairs * 4

        if has_center:
            result += 2
        return result
