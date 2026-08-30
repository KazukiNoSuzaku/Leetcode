# Author: Kaustav Ghosh
# Problem: Number of Single Divisor Triplets
# Approach: Values are small (1..100), so group by value frequency and iterate over unordered value multisets a<=b<=c. A multiset qualifies when exactly one of the three values divides their sum. For each qualifying multiset, add the number of ordered distinct-index triples it produces (accounting for repeated values)

from collections import Counter


class Solution(object):
    def singleDivisorTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = Counter(nums)
        vals = sorted(freq)
        total = 0
        for x in range(len(vals)):
            a = vals[x]
            for y in range(x, len(vals)):
                b = vals[y]
                for z in range(y, len(vals)):
                    c = vals[z]
                    s = a + b + c
                    divisors = (s % a == 0) + (s % b == 0) + (s % c == 0)
                    if divisors != 1:
                        continue
                    fa, fb, fc = freq[a], freq[b], freq[c]
                    if a != b and b != c:  # all distinct
                        ways = 6 * fa * fb * fc
                    elif a == b == c:      # all same
                        ways = fa * (fa - 1) * (fa - 2)
                    elif a == b:           # a == b != c
                        ways = 3 * fa * (fa - 1) * fc
                    else:                  # b == c != a
                        ways = 3 * fb * (fb - 1) * fa
                    total += ways
        return total
