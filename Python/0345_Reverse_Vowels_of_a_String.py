# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases.

# Example 1:
# Input: s = "IceCreAm"
# Output: "AceCreIm"

# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"

# Constraints:
# 1 <= s.length <= 3 * 10^5
# s consists of printable ASCII characters.

# Author: Kaustav Ghosh

class Solution(object):
    def reverseVowels(self, s):
        vowels = set('aeiouAEIOU')
        s = list(s)
        lo, hi = 0, len(s) - 1
        while lo < hi:
            while lo < hi and s[lo] not in vowels:
                lo += 1
            while lo < hi and s[hi] not in vowels:
                hi -= 1
            s[lo], s[hi] = s[hi], s[lo]
            lo += 1
            hi -= 1
        return ''.join(s)
