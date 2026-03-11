# Given a string s, reverse the order of characters in each word within a sentence while
# still preserving whitespace and initial word order.

# Author: Kaustav Ghosh

class Solution(object):
    def reverseWords(self, s):
        return ' '.join(w[::-1] for w in s.split())
