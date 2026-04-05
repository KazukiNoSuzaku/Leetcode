# Author: Kaustav Ghosh
# 2209. Minimum White Tiles After Covering With Carpets
# https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/
# Difficulty: Hard
#
# Approach: DP with prefix sums.
# Let prefix[i] = number of white tiles in floor[0..i-1].
# dp[i][j] = minimum white tiles visible in floor[0..i-1] using j carpets.
#
# Transitions (1-indexed carpets, 0-indexed floor):
#   Option 1: Don't place carpet ending at i -> dp[i][j] = dp[i-1][j] + (floor[i-1]=='1')
#   Option 2: Place a carpet ending at i     -> dp[i][j] = dp[max(0, i-carpetLen)][j-1]
#             (the carpet covers floor[i-carpetLen .. i-1], zero cost for those tiles)
# Take the minimum of both options.

class Solution(object):
    def minimumWhiteTiles(self, floor, numCarpets, carpetLen):
        """
        :type floor: str
        :type numCarpets: int
        :type carpetLen: int
        :rtype: int
        """
        n = len(floor)

        # prefix[i] = white tiles in floor[0..i-1]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + (1 if floor[i] == '1' else 0)

        # dp[i][j]: min white tiles visible considering first i tiles using j carpets
        # We use space optimisation: two 1D arrays
        # dp[j] = min white tiles in floor[0..i-1] with j carpets available
        INF = float('inf')
        # Initialize: 0 carpets -> all white tiles visible
        prev = [prefix[i] for i in range(n + 1)]  # prev[i] = white tiles in [0..i-1], 0 carpets

        for j in range(1, numCarpets + 1):
            curr = [0] * (n + 1)
            for i in range(1, n + 1):
                # Option 1: no carpet ending at position i
                opt1 = curr[i - 1] + (1 if floor[i - 1] == '1' else 0)
                # Option 2: place carpet covering [i-carpetLen .. i-1]
                start = max(0, i - carpetLen)
                opt2 = prev[start]
                curr[i] = min(opt1, opt2)
            prev = curr

        return prev[n]
