# Author: Kaustav Ghosh
# Problem 1986: Minimum Number of Work Sessions to Finish the Tasks

class Solution(object):
    def minSessions(self, tasks, sessionTime):
        """
        :type tasks: List[int]
        :type sessionTime: int
        :rtype: int
        """
        n = len(tasks)
        # Precompute subset sums
        subset_sum = [0] * (1 << n)
        for mask in range(1, 1 << n):
            bit = mask & (-mask)
            idx = bit.bit_length() - 1
            subset_sum[mask] = subset_sum[mask ^ bit] + tasks[idx]

        # Find all valid subsets (fit in one session)
        valid = []
        for mask in range(1, 1 << n):
            if subset_sum[mask] <= sessionTime:
                valid.append(mask)

        full = (1 << n) - 1
        # dp[mask] = min sessions to complete tasks in mask
        dp = [float('inf')] * (1 << n)
        dp[0] = 0

        for mask in range(1, 1 << n):
            # Enumerate submasks
            sub = mask
            while sub > 0:
                if subset_sum[sub] <= sessionTime:
                    dp[mask] = min(dp[mask], dp[mask ^ sub] + 1)
                sub = (sub - 1) & mask

        return dp[full]
