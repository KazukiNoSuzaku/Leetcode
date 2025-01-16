# Given a string s, return the longest 
# palindromic
 
# substring
#  in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

# Author: Kaustav Ghosh

class Solution(object):
    def longestPalindrome(self, s):
        def expandAroundCenter(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right

        if not s or len(s) == 0:
            return ""
        
        start, end = 0, 0
        for i in range(len(s)):
            l1, r1 = expandAroundCenter(s, i, i)  # Odd length palindromes
            l2, r2 = expandAroundCenter(s, i, i + 1)  # Even length palindromes
            
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2
        
        return s[start:end]
