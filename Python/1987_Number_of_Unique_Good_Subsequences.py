# Author: Kaustav Ghosh
# Problem 1987: Number of Unique Good Subsequences

class Solution(object):
    def numberOfUniqueGoodSubsequences(self, binary):
        """
        :type binary: str
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        # ends0 = count of unique subsequences ending with '0'
        # ends1 = count of unique subsequences ending with '1'
        ends0 = 0
        ends1 = 0
        has_zero = 0
        for ch in binary:
            if ch == '0':
                ends0 = (ends0 + ends1) % MOD
                has_zero = 1
            else:
                ends1 = (ends0 + ends1 + 1) % MOD
        return (ends0 + ends1 + has_zero) % MOD
