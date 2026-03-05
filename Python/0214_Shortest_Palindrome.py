# You are given a string s. You can convert s to a palindrome by adding characters in front of it.
# Return the shortest palindrome you can find by performing this transformation.

# Example 1:
# Input: s = "aacecaaa"
# Output: "aaacecaaa"

# Example 2:
# Input: s = "abcd"
# Output: "dcbabcd"

# Constraints:
# 0 <= s.length <= 5 * 10^4
# s consists of lowercase English letters only.

# Author: Kaustav Ghosh

class Solution(object):
    def shortestPalindrome(self, s):
        # Use KMP failure function on s + '#' + reverse(s)
        rev = s[::-1]
        combined = s + '#' + rev
        n = len(combined)
        fail = [0] * n
        j = 0
        for i in range(1, n):
            while j > 0 and combined[i] != combined[j]:
                j = fail[j - 1]
            if combined[i] == combined[j]:
                j += 1
            fail[i] = j
        longest_prefix = fail[-1]
        return rev[:len(s) - longest_prefix] + s
