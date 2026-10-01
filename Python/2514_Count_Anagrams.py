# Author: Kaustav Ghosh
# Problem: Count Anagrams
# Approach: Words are independent, so multiply their counts. A word of length L with letter multiplicities c gives L! / product(c!) distinct arrangements, computed modulo 1e9 + 7 with modular inverses of the factorials

from collections import Counter


class Solution(object):
    def countAnagrams(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        total = 1
        for word in s.split():
            factorial = 1
            for i in range(1, len(word) + 1):
                factorial = factorial * i % MOD
            for count in Counter(word).values():
                for i in range(1, count + 1):
                    factorial = factorial * pow(i, MOD - 2, MOD) % MOD
            total = total * factorial % MOD
        return total
