# Author: Kaustav Ghosh
# Problem: Maximum Number of Non-overlapping Palindrome Substrings
# Approach: Any palindrome of length at least k contains a palindrome of length exactly k or k + 1 at its centre, so only those two lengths need checking. Sweep left to right and take the first qualifying piece that starts at or after the last one ended, since finishing a piece as early as possible never costs a later one

class Solution(object):
    def maxPalindromes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = 0
        available = 0
        for end in range(len(s)):
            for length in (k, k + 1):
                start = end - length + 1
                if start >= available and s[start:end + 1] == s[start:end + 1][::-1]:
                    count += 1
                    available = end + 1
                    break
        return count
