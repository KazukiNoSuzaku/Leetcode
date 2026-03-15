# String contains only 'a' and 'b'. Remove palindromic subsequences to empty it.
# Answer is always 0 (empty), 1 (already palindrome), or 2 (at most 2 steps).

# Author: Kaustav Ghosh

class Solution(object):
    def removePalindromeSub(self, s):
        if not s: return 0
        if s == s[::-1]: return 1
        return 2
