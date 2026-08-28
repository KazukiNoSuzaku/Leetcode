# Author: Kaustav Ghosh
# Problem: Find Substring With Given Hash Value
# Approach: Rolling the hash left-to-right would require dividing by power (a modular inverse), so instead roll from the right. Compute the last window's hash directly, then extend leftward with H(i) = val(s[i]) + power*H(i+1) - val(s[i+k])*power^k, tracking the leftmost match

class Solution(object):
    def subStrHash(self, s, power, modulo, k, hashValue):
        """
        :type s: str
        :type power: int
        :type modulo: int
        :type k: int
        :type hashValue: int
        :rtype: str
        """
        def val(c):
            return ord(c) - ord('a') + 1

        n = len(s)
        pk = pow(power, k, modulo)

        # hash of the last window s[n-k : n]
        h = 0
        for t in range(k):
            h = (h + val(s[n - k + t]) * pow(power, t, modulo)) % modulo

        ans = n - k if h == hashValue else -1
        for i in range(n - k - 1, -1, -1):
            h = (val(s[i]) + power * h - val(s[i + k]) * pk) % modulo
            if h == hashValue:
                ans = i
        return s[ans:ans + k]
