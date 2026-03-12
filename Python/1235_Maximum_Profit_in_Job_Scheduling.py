# Author: Kaustav Ghosh
# DP with binary search: sort by end time, dp[i] = max profit considering first i jobs

class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        import bisect
        jobs = sorted(zip(endTime, startTime, profit))
        ends = [j[0] for j in jobs]
        n = len(jobs)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            end, start, prof = jobs[i - 1]
            # Find last job that ends <= start
            k = bisect.bisect_right(ends, start, 0, i - 1)
            dp[i] = max(dp[i - 1], dp[k] + prof)
        return dp[n]
