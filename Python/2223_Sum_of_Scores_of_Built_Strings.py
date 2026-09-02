# Author: Kaustav Ghosh
# Problem: Sum of Scores of Built Strings
# Approach: The strings built by prepending characters are exactly the suffixes of s, and each score is the longest common prefix between a suffix and the whole string. That is precisely the Z-array of s (with Z[0] = n), so the answer is the sum of all Z values

class Solution(object):
    def sumScores(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        z = [0] * n
        z[0] = n
        l = r = 0
        for i in range(1, n):
            if i < r:
                z[i] = min(r - i, z[i - l])
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] > r:
                l, r = i, i + z[i]
        return sum(z)
