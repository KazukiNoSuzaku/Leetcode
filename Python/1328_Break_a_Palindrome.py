# Replace one character in a palindrome string to make it the lexicographically
# smallest non-palindrome. Return "" if length is 1.

# Author: Kaustav Ghosh

class Solution(object):
    def breakPalindrome(self, palindrome):
        n = len(palindrome)
        if n == 1:
            return ""
        s = list(palindrome)
        for i in range(n // 2):
            if s[i] != 'a':
                s[i] = 'a'
                return ''.join(s)
        s[-1] = 'b'
        return ''.join(s)
