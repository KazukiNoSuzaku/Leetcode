# We can scramble a string s to get a string t using the following algorithm:
# 1. If the length of the string is 1, stop.
# 2. Split the string into two non-empty substrings at a random index.
# 3. Randomly decide to swap or not swap the two substrings.
# 4. Apply this recursively on both substrings.
# Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1.

# Example 1:
# Input: s1 = "great", s2 = "rgeat"
# Output: true

# Example 2:
# Input: s1 = "abcde", s2 = "caebd"
# Output: false

# Constraints:
# s1.length == s2.length
# 1 <= s1.length <= 30
# s1 and s2 consist of lowercase English letters.

# Author: Kaustav Ghosh

class Solution(object):
    def isScramble(self, s1, s2):
        memo = {}

        def dp(a, b):
            if (a, b) in memo:
                return memo[(a, b)]
            if a == b:
                return True
            if sorted(a) != sorted(b):
                return False
            n = len(a)
            for i in range(1, n):
                # No swap
                if dp(a[:i], b[:i]) and dp(a[i:], b[i:]):
                    memo[(a, b)] = True
                    return True
                # Swap
                if dp(a[:i], b[n-i:]) and dp(a[i:], b[:n-i]):
                    memo[(a, b)] = True
                    return True
            memo[(a, b)] = False
            return False

        return dp(s1, s2)
