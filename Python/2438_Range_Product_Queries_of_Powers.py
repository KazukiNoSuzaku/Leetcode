# Author: Kaustav Ghosh
# Problem: Range Product Queries of Powers
# Approach: The minimal set of powers summing to n is just the set bits of n, in increasing order. Every term is a power of two, so a range product is 2 raised to the sum of the exponents in that range, which a prefix sum of exponents answers per query without any modular division

class Solution(object):
    def productQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10 ** 9 + 7
        exponents = [bit for bit in range(31) if n >> bit & 1]
        prefix = [0]
        for exponent in exponents:
            prefix.append(prefix[-1] + exponent)
        return [pow(2, prefix[right + 1] - prefix[left], MOD) for left, right in queries]
