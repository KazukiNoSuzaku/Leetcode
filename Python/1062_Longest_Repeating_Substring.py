# Author: Kaustav Ghosh
# 1062. Longest Repeating Substring
# https://leetcode.com/problems/longest-repeating-substring/

class Solution(object):
    def longestRepeatingSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        MOD = (1 << 61) - 1
        BASE = 31

        def check(length):
            h = 0
            power = 1
            for i in range(length):
                h = (h * BASE + ord(s[i])) % MOD
                if i < length - 1:
                    power = (power * BASE) % MOD
            seen = {h: [0]}
            for i in range(1, n - length + 1):
                h = (h - ord(s[i-1]) * power) % MOD
                h = (h * BASE + ord(s[i + length - 1])) % MOD
                if h in seen:
                    sub = s[i:i+length]
                    for j in seen[h]:
                        if s[j:j+length] == sub:
                            return True
                    seen[h].append(i)
                else:
                    seen[h] = [i]
            return False

        lo, hi = 0, n - 1
        result = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                result = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return result
