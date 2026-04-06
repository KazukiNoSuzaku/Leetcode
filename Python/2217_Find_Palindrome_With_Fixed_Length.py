# Author: Kaustav Ghosh
# Problem: 2217. Find Palindrome With Fixed Length
# URL: https://leetcode.com/problems/find-palindrome-with-fixed-length/
# Difficulty: Medium
#
# Approach:
# The k-digit palindromes are formed by their first ceil(k/2) digits.
# The smallest k-digit palindrome corresponds to half = 10^(half_len-1),
# and successive ones are half+1, half+2, ...
# For query index (1-based), the half value is start + (index-1).
# Mirror the half to form the full palindrome. If the half overflows
# (>= 10^half_len), return -1.

class Solution(object):
    def kthPalindrome(self, queries, intLength):
        """
        :type queries: list[int]
        :type intLength: int
        :rtype: list[int]
        """
        half_len = (intLength + 1) // 2
        start = 10 ** (half_len - 1)
        limit = 10 ** half_len

        result = []
        for q in queries:
            half = start + q - 1
            if half >= limit:
                result.append(-1)
                continue
            half_str = str(half)
            if intLength % 2 == 0:
                palindrome = half_str + half_str[::-1]
            else:
                palindrome = half_str + half_str[-2::-1]
            result.append(int(palindrome))
        return result
