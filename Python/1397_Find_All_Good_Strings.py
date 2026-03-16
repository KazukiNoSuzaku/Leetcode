# Author: Kaustav Ghosh
# Problem: Find All Good Strings (Premium)
# Approach: Digit DP with KMP automaton to count strings in [s1, s2] not containing evil

class Solution(object):
    def findGoodStrings(self, n, s1, s2, evil):
        """
        :type n: int
        :type s1: str
        :type s2: str
        :type evil: str
        :rtype: int
        """
        MOD = 10**9 + 7
        m = len(evil)

        # Build KMP failure function
        lps = [0] * m
        length = 0
        i = 1
        while i < m:
            if evil[i] == evil[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length:
                length = lps[length - 1]
            else:
                i += 1

        # Build KMP transition table
        goto = [[0] * 26 for _ in range(m)]
        for state in range(m):
            for c in range(26):
                ch = chr(c + ord('a'))
                j = state
                while j > 0 and evil[j] != ch:
                    j = lps[j - 1]
                if evil[j] == ch:
                    j += 1
                goto[state][c] = j

        memo = {}

        def count(s):
            # Count good strings <= s
            def dp(pos, kmp_state, tight):
                if kmp_state == m:
                    return 0
                if pos == n:
                    return 1
                if (pos, kmp_state, tight) in memo:
                    return memo[(pos, kmp_state, tight)]
                limit = ord(s[pos]) - ord('a') if tight else 25
                result = 0
                for c in range(limit + 1):
                    new_state = goto[kmp_state][c]
                    new_tight = tight and (c == limit)
                    result = (result + dp(pos + 1, new_state, new_tight)) % MOD
                memo[(pos, kmp_state, tight)] = result
                return result

            memo.clear()
            return dp(0, 0, True)

        ans = (count(s2) - count(s1) + MOD) % MOD

        # Check if s1 itself is good (doesn't contain evil)
        j = 0
        for c in s1:
            while j > 0 and evil[j] != c:
                j = lps[j - 1]
            if evil[j] == c:
                j += 1
            if j == m:
                break
        else:
            ans = (ans + 1) % MOD

        return ans
