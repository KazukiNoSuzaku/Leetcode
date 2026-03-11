# Partition array into at most k groups to maximize sum of averages.

# Author: Kaustav Ghosh

class Solution(object):
    def largestSumOfAverages(self, nums, k):
        n = len(nums)
        prefix = [0] * (n + 1)
        for i, x in enumerate(nums): prefix[i+1] = prefix[i] + x
        def avg(i, j): return (prefix[j] - prefix[i]) / float(j - i)
        dp = [avg(0, i+1) for i in range(n)]
        for _ in range(k - 1):
            new_dp = dp[:]
            for j in range(n):
                for i in range(j):
                    new_dp[j] = max(new_dp[j], dp[i] + avg(i+1, j+1))
            dp = new_dp
        return dp[-1]
