# Author: Kaustav Ghosh
# Problem: Remove All Occurrences of a Substring
# Approach: Build the result on a stack one character at a time; whenever the last len(part) characters equal part, pop them off. This removes every occurrence, including ones newly formed by earlier removals

class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        k = len(part)
        stack = []
        for ch in s:
            stack.append(ch)
            if len(stack) >= k and stack[-k:] == list(part):
                del stack[-k:]
        return ''.join(stack)
