# Author: Kaustav Ghosh

class Solution(object):
    def makeStringSorted(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        n = len(s)
        # Precompute factorials and inverse factorials
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (n + 1)
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n - 1, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        count = [0] * 26
        res = 0
        for i in range(n - 1, -1, -1):
            c = ord(s[i]) - ord('a')
            count[c] += 1
            # Number of chars smaller than s[i] to the right
            smaller = sum(count[:c])
            # Permutations of remaining chars
            perm = smaller * fact[n - 1 - i] % MOD
            for j in range(26):
                perm = perm * inv_fact[count[j]] % MOD
            res = (res + perm) % MOD
        return res
