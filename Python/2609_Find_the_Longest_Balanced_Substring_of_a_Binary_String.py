class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        ans = i = 0
        n = len(s)
        while i < n:
            zeros = 0
            while i < n and s[i] == '0':
                zeros += 1
                i += 1
            ones = 0
            while i < n and s[i] == '1':
                ones += 1
                i += 1
            ans = max(ans, 2 * min(zeros, ones))
        return ans
