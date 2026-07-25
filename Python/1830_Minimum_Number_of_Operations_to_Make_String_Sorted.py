# Author: Kaustav Ghosh
# Problem: Minimum Number of Operations to Make String Sorted
# Approach: The described operation is a previous-permutation step, so the answer is s's 0-indexed rank among its distinct permutations. Compute that rank with the multiset-permutation formula and factorials mod p

class Solution(object):
    def makeStringSorted(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        n = len(s)

        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        inv_fact = [1] * (n + 1)
        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n - 1, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        count = [0] * 26
        for c in s:
            count[ord(c) - 97] += 1

        rank = 0
        for i in range(n):
            c = ord(s[i]) - 97
            smaller = sum(count[j] for j in range(c))
            # permutations of the remaining multiset starting with a smaller letter
            perms = fact[n - i - 1]
            for j in range(26):
                perms = perms * inv_fact[count[j]] % MOD
            rank = (rank + smaller * perms) % MOD
            count[c] -= 1

        return rank
