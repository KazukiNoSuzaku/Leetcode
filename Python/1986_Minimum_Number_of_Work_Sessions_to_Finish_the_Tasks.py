# Author: Kaustav Ghosh
# Problem: Minimum Number of Work Sessions to Finish the Tasks
# Approach: Bitmask DP over the set of finished tasks. Each state stores the lexicographically best (session count, time used in the current session). Adding a task either fits in the current session or opens a new one; fewer sessions and then less used time is preferred

class Solution(object):
    def minSessions(self, tasks, sessionTime):
        """
        :type tasks: List[int]
        :type sessionTime: int
        :rtype: int
        """
        n = len(tasks)
        full = (1 << n) - 1
        INF = (float('inf'), float('inf'))
        dp = [INF] * (1 << n)
        dp[0] = (1, 0)
        for mask in range(1 << n):
            sessions, used = dp[mask]
            if sessions == float('inf'):
                continue
            for i in range(n):
                if mask >> i & 1:
                    continue
                nm = mask | (1 << i)
                if used + tasks[i] <= sessionTime:
                    cand = (sessions, used + tasks[i])
                else:
                    cand = (sessions + 1, tasks[i])
                if cand < dp[nm]:
                    dp[nm] = cand
        return dp[full][0]
