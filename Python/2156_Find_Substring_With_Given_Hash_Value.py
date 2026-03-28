# Author: Kaustav Ghosh
# Problem: 2156. Find Substring With Given Hash Value
# URL: https://leetcode.com/problems/find-substring-with-given-hash-value/
# Approach: Rolling hash computed backwards to avoid mod of negative numbers
# hash(s, p, m, k, i) = sum(val(s[i+j]) * p^j) % m for j in [0, k-1]
# Process from right to left: hash_prev = (hash_cur + val(s[i]) * p^(k-1)) % m

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
        n = len(s)
        # precompute power^(k-1) % modulo
        pk = pow(power, k - 1, modulo)
        cur_hash = 0
        ans_start = 0

        # compute hash of last window s[n-k..n-1]
        for i in range(n - 1, n - k - 1, -1):
            cur_hash = (cur_hash * power + (ord(s[i]) - ord('a') + 1)) % modulo

        if cur_hash == hashValue:
            ans_start = n - k

        # slide window backwards
        for i in range(n - k - 1, -1, -1):
            # add s[i] at front, remove s[i+k] at back
            cur_hash = (cur_hash - (ord(s[i + k]) - ord('a') + 1) * pk % modulo + modulo) % modulo
            cur_hash = (cur_hash * power + (ord(s[i]) - ord('a') + 1)) % modulo
            if cur_hash == hashValue:
                ans_start = i

        return s[ans_start:ans_start + k]
