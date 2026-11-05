# Author: Kaustav Ghosh
# Problem: Minimum Number of Operations to Make String Sorted
# Approach: The stated operation is exactly the step that produces the previous permutation in lexicographic order, so repeating it until the string is sorted takes as many steps as there are arrangements of these letters strictly smaller than the given one. That count is the string's rank, computed position by position: fixing a smaller letter at the current position leaves the remaining letters free, which is a multinomial coefficient over their counts. Dividing by the repeated-letter factorials is done with modular inverses, and the denominator is carried along and corrected by one multiplication per position instead of being rebuilt, so the whole rank costs one pass over the string times the alphabet.

class Solution(object):
    def makeStringSorted(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter

        MOD = 10 ** 9 + 7
        n = len(s)

        factorial = [1] * (n + 1)
        for i in range(1, n + 1):
            factorial[i] = factorial[i - 1] * i % MOD
        inverse_factorial = [1] * (n + 1)
        inverse_factorial[n] = pow(factorial[n], MOD - 2, MOD)
        for i in range(n, 0, -1):
            inverse_factorial[i - 1] = inverse_factorial[i] * i % MOD

        remaining = Counter(s)
        # One over the product of the factorials of the remaining letter counts.
        spread = 1
        for count in remaining.values():
            spread = spread * inverse_factorial[count] % MOD

        rank = 0
        for position, letter in enumerate(s):
            smaller = sum(count for other, count in remaining.items() if other < letter)
            if smaller:
                rank = (rank + smaller * factorial[n - position - 1] % MOD * spread) % MOD
            spread = spread * remaining[letter] % MOD
            remaining[letter] -= 1
            if not remaining[letter]:
                del remaining[letter]
        return rank
