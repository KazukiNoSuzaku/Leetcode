# Author: Kaustav Ghosh

class Solution(object):
    def minSideJumps(self, obstacles):
        """
        :type obstacles: List[int]
        :rtype: int
        """
        n = len(obstacles)
        # dp[lane] = min side jumps to reach current position in that lane
        dp = [1, 0, 1]  # start at lane 2 (index 1)
        for i in range(1, n):
            # Block lanes with obstacles
            new_dp = [float('inf')] * 3
            for j in range(3):
                if obstacles[i] == j + 1:
                    new_dp[j] = float('inf')
                else:
                    new_dp[j] = dp[j]
            # Try side jumps
            for j in range(3):
                if obstacles[i] == j + 1:
                    continue
                for k in range(3):
                    if k != j and obstacles[i] != k + 1:
                        new_dp[j] = min(new_dp[j], new_dp[k] + 1)
            dp = new_dp
        return min(dp)
