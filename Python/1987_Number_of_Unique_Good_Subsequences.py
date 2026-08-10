# Author: Kaustav Ghosh
# Problem: Number of Unique Good Subsequences
# Approach: Count distinct subsequences that start with '1' by tracking how many end in 0 and end in 1. A '1' extends all of them and also forms the standalone "1"; a '0' only extends existing ones. Finally add one for the lone "0" if any zero exists

class Solution(object):
    def numberOfUniqueGoodSubsequences(self, binary):
        """
        :type binary: str
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        end0 = end1 = 0
        has_zero = False
        for c in binary:
            if c == '1':
                end1 = (end0 + end1 + 1) % MOD
            else:
                end0 = (end0 + end1) % MOD
                has_zero = True
        return (end0 + end1 + (1 if has_zero else 0)) % MOD
