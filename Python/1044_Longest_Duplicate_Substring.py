# Author: Kaustav Ghosh
# 1044. Longest Duplicate Substring
# https://leetcode.com/problems/longest-duplicate-substring/

class Solution(object):
    def longestDupSubstring(self, s):
        """
        :type s: str
        :rtype: str
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
                            return sub
                    seen[h].append(i)
                else:
                    seen[h] = [i]
            return ""

        lo, hi = 1, n - 1
        result = ""
        while lo <= hi:
            mid = (lo + hi) // 2
            found = check(mid)
            if found:
                result = found
                lo = mid + 1
            else:
                hi = mid - 1
        return result
