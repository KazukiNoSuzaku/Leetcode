# Author: Kaustav Ghosh
# Problem: Count Number of Special Subsequences
# Approach: A special subsequence is a block of zeros, then a block of ones, then a block of twos, each non-empty, so a partial subsequence is in exactly one of three stages and only needs to be counted, not stored. Sweeping the array I keep how many partial subsequences sit in each stage. A zero either joins or is skipped by every zeros-only subsequence and can also start a new one, so that stage doubles and gains one. A one either joins or is skipped by every subsequence already in the ones stage, and can also be the first one appended to any zeros-only subsequence, so that stage doubles and gains the zeros count. A two behaves the same way against the ones stage. The answer is the third stage's count after one pass, taken modulo 10^9 + 7.

class Solution(object):
    def countSpecialSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        zeros = ones = twos = 0
        for value in nums:
            if value == 0:
                zeros = (2 * zeros + 1) % MOD
            elif value == 1:
                ones = (2 * ones + zeros) % MOD
            else:
                twos = (2 * twos + ones) % MOD
        return twos
