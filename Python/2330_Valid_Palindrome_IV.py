# Author: Kaustav Ghosh
# Problem: 2330. Valid Palindrome IV
# URL: https://leetcode.com/problems/valid-palindrome-iv/
# Difficulty: Medium
# Note: Premium problem
#
# Approach:
# Use two pointers from both ends. Count positions where s[i] != s[j].
# Each mismatch requires one replacement (change either s[i] or s[j]).
# We are allowed exactly 2 operations (replacements). So if mismatches <= 2, return True.

class Solution(object):
    def makePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mismatches = 0
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                mismatches += 1
            left += 1
            right -= 1
        return mismatches <= 2
