class Solution:
    def monkeyMove(self, n: int) -> int:
        # Total arrangements = 2^n; only 2 are collision-free (all clockwise or all counterclockwise).
        MOD = 10 ** 9 + 7
        return (pow(2, n, MOD) - 2) % MOD
