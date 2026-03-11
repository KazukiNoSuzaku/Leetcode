# Given a positive integer n, return the number of the integers in the range [0, n]
# whose binary representations do not contain consecutive ones.

# Author: Kaustav Ghosh

class Solution(object):
    def findIntegers(self, n):
        bits = bin(n)[2:]
        m = len(bits)
        # dp[i][j]: count of valid i-bit numbers ending with bit j
        dp = [[1, 1]] + [[0, 0]] * (m - 1)
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + dp[i-1][1]
            dp[i][1] = dp[i-1][0]
        res = dp[m-1][0] + dp[m-1][1]
        for i in range(1, m):
            if bits[i] == '1' and bits[i-1] == '1':
                break
            if bits[i] == '0' and bits[i-1] == '0':
                res -= dp[m-1-i][1]
        return res
