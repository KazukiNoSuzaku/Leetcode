# Author: Kaustav Ghosh

class Solution(object):
    def minChanges(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import Counter
        n = len(nums)
        # Group nums by position mod k
        groups = []
        for i in range(k):
            cnt = Counter()
            for j in range(i, n, k):
                cnt[nums[j]] += 1
            groups.append(cnt)

        MAX_VAL = 1024
        INF = float('inf')
        # dp[xor_val] = min changes to make first i groups have XOR = xor_val
        dp = [INF] * MAX_VAL
        dp[0] = 0

        for i in range(k):
            group_size = sum(groups[i].values())
            # Best from previous dp
            min_prev = min(dp)
            new_dp = [min_prev + group_size] * MAX_VAL
            for xor_val in range(MAX_VAL):
                if dp[xor_val] == INF:
                    continue
                for val, cnt in groups[i].items():
                    new_xor = xor_val ^ val
                    new_dp[new_xor] = min(new_dp[new_xor], dp[xor_val] + group_size - cnt)
            dp = new_dp
        return dp[0]
