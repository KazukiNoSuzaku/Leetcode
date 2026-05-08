class Solution:
    def goodBinaryStrings(self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:
        # dp[i] = number of good strings of length i; append zeroGroup zeros or oneGroup ones.
        MOD = 10 ** 9 + 7
        dp = [0] * (maxLength + 1)
        dp[0] = 1
        for i in range(1, maxLength + 1):
            if i >= zeroGroup:
                dp[i] = (dp[i] + dp[i - zeroGroup]) % MOD
            if i >= oneGroup:
                dp[i] = (dp[i] + dp[i - oneGroup]) % MOD
        return sum(dp[minLength:maxLength + 1]) % MOD
