# Count ways to decode a string that may contain '*' (wildcard for 1-9). Answer mod 10^9+7.

# Author: Kaustav Ghosh

class Solution(object):
    def numDecodings(self, s):
        MOD = 10**9 + 7
        dp1, dp2 = 1, 0  # dp1: ways ending single, dp2: ways ending two-char
        for ch in s:
            if ch == '*':
                new1 = 9 * dp1 % MOD
                new2 = (2 * dp2 + 15 * dp1) % MOD  # depends on prev
                # Actually track properly
            else:
                new1 = dp1 if ch != '0' else 0
            dp1, dp2 = new1, 0

        # Proper DP
        MOD = 10**9 + 7
        prev2, prev1 = 1, (9 if s[0] == '*' else (0 if s[0] == '0' else 1))
        for i in range(1, len(s)):
            cur = 0
            c, p = s[i], s[i-1]
            # Single digit
            if c == '*': cur = 9 * prev1 % MOD
            elif c != '0': cur = prev1
            # Two digits
            if p == '*':
                if c == '*': cur = (cur + 15 * prev2) % MOD
                elif c <= '6': cur = (cur + 2 * prev2) % MOD
                else: cur = (cur + prev2) % MOD
            elif p == '1':
                if c == '*': cur = (cur + 9 * prev2) % MOD
                else: cur = (cur + prev2) % MOD
            elif p == '2':
                if c == '*': cur = (cur + 6 * prev2) % MOD
                elif c <= '6': cur = (cur + prev2) % MOD
            prev2, prev1 = prev1, cur
        return prev1
