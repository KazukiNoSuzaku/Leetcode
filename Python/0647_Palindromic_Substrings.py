# Count the number of palindromic substrings in a string.

# Author: Kaustav Ghosh

class Solution(object):
    def countSubstrings(self, s):
        count = 0
        n = len(s)
        for center in range(2 * n - 1):
            l, r = center // 2, (center + 1) // 2
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        return count
