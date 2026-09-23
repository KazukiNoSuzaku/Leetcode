# Author: Kaustav Ghosh
# Problem: Maximum Deletions on a String
# Approach: dp[i] is the most operations available on the suffix starting at i. Deleting a prefix of length L is allowed when the next L characters repeat it, which is a longest-common-prefix test between positions i and i + L. Those lengths follow the recurrence lcp(i, j) = lcp(i + 1, j + 1) + 1 when the characters match, so sweeping i downwards needs only the previous row. A string of one repeated character is the worst case for that scan and is answered directly

class Solution(object):
    def deleteString(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if len(set(s)) == 1:
            return n
        dp = [0] * (n + 1)
        previous = [0] * (n + 2)
        for i in range(n - 1, -1, -1):
            ch = s[i]
            current = [0] * (n + 2)
            current[i + 1:n] = [previous[j + 1] + 1 if s[j] == ch else 0
                                for j in range(i + 1, n)]
            best = 1
            for length in range(1, (n - i) // 2 + 1):
                if current[i + length] >= length:
                    best = max(best, 1 + dp[i + length])
            dp[i] = best
            previous = current
        return dp[0]
