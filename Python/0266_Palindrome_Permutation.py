# Given a string s, return true if a permutation of the string could form a palindrome
# and false otherwise.

# Example 1:
# Input: s = "code"
# Output: false

# Example 2:
# Input: s = "aab"
# Output: true

# Constraints:
# 1 <= s.length <= 5000
# s consists of only lowercase English letters.

# Author: Kaustav Ghosh

class Solution(object):
    def canPermutePalindrome(self, s):
        from collections import Counter
        return sum(v % 2 for v in Counter(s).values()) <= 1
