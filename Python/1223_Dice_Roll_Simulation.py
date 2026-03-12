# Author: Kaustav Ghosh
# DP with state (rolls_left, last_face, consecutive_count)

class Solution(object):
    def dieSimulator(self, n, rollMax):
        """
        :type n: int
        :type rollMax: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        # dp[face][consec] = number of sequences ending with face having consec consecutive
        dp = [[0] * 16 for _ in range(6)]
        for f in range(6):
            dp[f][1] = 1

        for roll in range(1, n):
            new_dp = [[0] * 16 for _ in range(6)]
            for f in range(6):
                for c in range(1, rollMax[f] + 1):
                    if dp[f][c] == 0:
                        continue
                    for nf in range(6):
                        if nf == f:
                            if c + 1 <= rollMax[f]:
                                new_dp[nf][c + 1] = (new_dp[nf][c + 1] + dp[f][c]) % MOD
                        else:
                            new_dp[nf][1] = (new_dp[nf][1] + dp[f][c]) % MOD
            dp = new_dp

        result = 0
        for f in range(6):
            for c in range(1, 16):
                result = (result + dp[f][c]) % MOD
        return result
