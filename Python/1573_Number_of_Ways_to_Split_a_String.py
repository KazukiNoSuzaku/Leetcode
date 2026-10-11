# Author: Kaustav Ghosh
# Problem: Number of Ways to Split a String
# Approach: Each part must hold the same number of ones, so the total count has to be divisible by three, and once it is, the first part must end somewhere between the k-th one and the one just before the (k+1)-th, with the two cut points chosen independently. That makes the answer the product of the two gaps measured between consecutive ones at the block boundaries. The all-zeros string is the exception: every one of the ones-based boundaries vanishes and any two of the n-1 cut positions work, giving (n-1)(n-2)/2.

class Solution(object):
    def numWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        ones = [i for i, ch in enumerate(s) if ch == '1']
        total = len(ones)
        if total % 3:
            return 0
        n = len(s)
        if total == 0:
            return (n - 1) * (n - 2) // 2 % MOD
        k = total // 3
        first_gap = ones[k] - ones[k - 1]
        second_gap = ones[2 * k] - ones[2 * k - 1]
        return first_gap * second_gap % MOD
