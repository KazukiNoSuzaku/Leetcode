from math import factorial
from collections import Counter

class Solution:
    def countAnagrams(self, s: str) -> int:
        # For each word, permutations = len! / product(freq[c]!); multiply across all words.
        MOD = 10**9 + 7
        ans = 1
        for word in s.split():
            ans = ans * factorial(len(word)) % MOD
            for cnt in Counter(word).values():
                ans = ans * pow(factorial(cnt), MOD - 2, MOD) % MOD
        return ans
