# Author: Kaustav Ghosh
# https://leetcode.com/problems/number-of-ways-to-separate-numbers/

class Solution(object):
    def numberOfCombinations(self, num):
        """
        :type num: str
        :rtype: int
        """
        if num[0] == '0':
            return 0
        MOD = 10 ** 9 + 7
        n = len(num)

        # lcp[i][j] = length of longest common prefix of num[i:] and num[j:]
        lcp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if num[i] == num[j]:
                    lcp[i][j] = lcp[i + 1][j + 1] + 1

        def compare(i, j, length):
            # Compare num[i:i+length] <= num[j:j+length]
            l = lcp[i][j]
            if l >= length:
                return True
            return num[i + l] <= num[j + l]

        # dp[i][j] = number of ways to partition num[0:i+1] where last number starts at j
        # and has length i - j + 1
        # prefix_dp[i][j] = sum of dp[i][0..j]
        # dp[i][j] valid if num[j] != '0' and last number >= previous number

        # Use prefix sum optimization
        # dp[i][j] where last segment is num[j..i] of length L = i-j+1
        # Previous segment ends at j-1 and has length <= L
        # Unless it has length == L, in which case num[prev_start..j-1] <= num[j..i]

        dp = [[0] * n for _ in range(n)]
        prefix = [[0] * (n + 1) for _ in range(n)]

        for i in range(n):
            for j in range(i + 1):
                length = i - j + 1
                if num[j] == '0':
                    dp[i][j] = 0
                elif j == 0:
                    dp[i][j] = 1
                else:
                    # Previous segment ends at j-1, has length <= length
                    # All segments of length < length starting from j - length + 1 ... to ...
                    # Previous start = j - prev_len, prev end = j - 1
                    # prev_len <= length => prev_start >= j - length
                    # Also prev_start >= 0 => prev_len <= j
                    # Sum dp[j-1][prev_start] for prev_start >= j - length + 1
                    # which is prefix[j-1][j] - prefix[j-1][j - length + 1 - 1]
                    # For shorter lengths: prev_start > j - length => prev_start from j-length+1 to j
                    # But prev_start must be <= j-1 for non-empty previous
                    short_start = max(0, j - length + 1)
                    dp[i][j] = (prefix[j - 1][j] - prefix[j - 1][max(0, short_start) - 1] if short_start > 0 else prefix[j - 1][j]) % MOD

                    # For equal length: prev_start = j - length, prev has length = length
                    if j - length >= 0 and num[j - length] != '0':
                        if compare(j - length, j, length):
                            dp[i][j] = (dp[i][j] + dp[j - 1][j - length]) % MOD
                        else:
                            # Already counted shorter, need to remove this
                            pass

            # Build prefix sums
            for j in range(n):
                prefix[i][j] = (prefix[i][j - 1] + dp[i][j]) % MOD if j > 0 else dp[i][0]

        return prefix[n - 1][n - 1] % MOD
