class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                s[l] = s[r] = min(s[l], s[r])
            l += 1
            r -= 1
        return ''.join(s)
